import os
import re
import sys
import subprocess

# Auto-install markdown library if not available
try:
    import markdown
except ImportError:
    print("Markdown library not found. Attempting to install...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown"])
    import markdown

def get_markdown_files():
    """Traverses domains/ and outputs/ to find all .md files (excluding README.md)."""
    docs = []
    # Directories to scan
    dirs_to_scan = ["domains", "outputs"]
    
    for base_dir in dirs_to_scan:
        if not os.path.exists(base_dir):
            continue
        for root, _, files in os.walk(base_dir):
            for file in files:
                if file.endswith(".md") and file != "README.md":
                    full_path = os.path.join(root, file)
                    # Create a friendly category name from the path
                    rel_path = os.path.relpath(root, base_dir)
                    category = base_dir.title()
                    if rel_path != ".":
                        category = rel_path.replace("-", " ").title()
                    
                    docs.append({
                        "full_path": full_path,
                        "rel_path": os.path.relpath(full_path, "."),
                        "filename": file,
                        "title": file.replace(".md", "").replace("-", " ").title(),
                        "category": category
                    })
    # Sort docs by category and title
    docs.sort(key=lambda x: (x["category"], x["title"]))
    return docs

def build_docs():
    docs = get_markdown_files()
    output_dir = "outputs/docs"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate sidebar data
    categories = {}
    for doc in docs:
        cat = doc["category"]
        if cat not in categories:
            categories[cat] = []
        # Target HTML filename
        html_filename = doc["rel_path"].replace("/", "_").replace(".md", ".html")
        categories[cat].append({
            "title": doc["title"],
            "url": html_filename,
            "filename": doc["filename"]
        })

    # Read each markdown file and compile it
    for doc in docs:
        with open(doc["full_path"], "r", encoding="utf-8") as f:
            md_content = f.read()
            
        # Parse titles from the first header if possible
        title_match = re.search(r"^#\s+(.*)", md_content, re.MULTILINE)
        doc_title = title_match.group(1).strip() if title_match else doc["title"]
        
        # Convert Markdown to HTML with extensions for tables, code blocks, etc.
        html_content = markdown.markdown(
            md_content,
            extensions=["extra", "codehilite", "toc", "tables", "fenced_code"]
        )
        
        # Build the final page wrapper
        wrapped_html = get_html_template(doc_title, html_content, categories, doc["rel_path"])
        
        # Write to outputs/docs/
        dest_filename = doc["rel_path"].replace("/", "_").replace(".md", ".html")
        dest_path = os.path.join(output_dir, dest_filename)
        with open(dest_path, "w", encoding="utf-8") as out_f:
            out_f.write(wrapped_html)
        print(f"Compiled {doc['full_path']} -> {dest_path}")

    # Generate index.html redirecting to the first available doc, or showing a welcome dashboard
    welcome_html = get_welcome_page(categories)
    index_path = os.path.join(output_dir, "index.html")
    with open(index_path, "w", encoding="utf-8") as out_f:
        out_f.write(welcome_html)
    print(f"Generated Index Portal: {index_path}")

def get_html_template(title, body, categories, active_rel_path=""):
    # Generate sidebar HTML
    sidebar_html = ""
    active_html_name = active_rel_path.replace("/", "_").replace(".md", ".html")
    
    for cat, items in sorted(categories.items()):
        sidebar_html += f'<div class="mb-4"><h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">{cat}</h3><ul class="space-y-1">'
        for item in items:
            is_active = item["url"] == active_html_name
            active_class = "bg-sky-600 text-white font-medium" if is_active else "text-slate-300 hover:bg-slate-700 hover:text-white"
            sidebar_html += f'<li><a href="{item["url"]}" class="block px-3 py-1.5 rounded-md text-sm transition-colors {active_class}">{item["title"]}</a></li>'
        sidebar_html += '</ul></div>'

    return f"""<!DOCTYPE html>
<html lang="zh-TW" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Jerry's Growth Docs</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        slate: {{
                            950: '#0b1329'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <!-- Prism.js CSS for modern code highlighting -->
    <link href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/themes/prism-tomorrow.min.css" rel="stylesheet" />
    <style>
        /* Custom scrollbars */
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: #1e293b;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #475569;
            border-radius: 3px;
        }}
        ::-webkit-scrollbar-thumb:hover {{
            background: #64748b;
        }}
        /* Markdown rendering overrides */
        .markdown-body h1 {{ @apply text-3xl font-bold text-white mb-6 border-b border-slate-700 pb-2; }}
        .markdown-body h2 {{ @apply text-2xl font-bold text-sky-400 mt-8 mb-4 border-b border-slate-800 pb-1; }}
        .markdown-body h3 {{ @apply text-xl font-semibold text-sky-300 mt-6 mb-3; }}
        .markdown-body p {{ @apply text-slate-300 mb-4 leading-relaxed; }}
        .markdown-body ul {{ @apply list-disc list-inside text-slate-300 mb-4 pl-4 space-y-2; }}
        .markdown-body ol {{ @apply list-decimal list-inside text-slate-300 mb-4 pl-4 space-y-2; }}
        .markdown-body blockquote {{ @apply border-l-4 border-sky-500 bg-slate-800/50 px-4 py-3 rounded-r-md text-slate-400 italic my-4; }}
        .markdown-body table {{ @apply min-w-full divide-y divide-slate-800 my-6; }}
        .markdown-body th {{ @apply bg-slate-800/50 text-left px-4 py-3 text-xs font-semibold text-sky-400 uppercase tracking-wider border-b border-slate-700; }}
        .markdown-body td {{ @apply px-4 py-3 text-sm text-slate-300 border-b border-slate-800/50; }}
        .markdown-body pre {{ @apply rounded-lg p-4 bg-slate-900 overflow-x-auto my-4 border border-slate-800; }}
        .markdown-body code {{ @apply text-sky-300 bg-slate-800 px-1.5 py-0.5 rounded text-sm font-mono; }}
        .markdown-body pre code {{ @apply text-inherit bg-inherit p-0; }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans">
    <!-- Top Navbar -->
    <header class="bg-slate-900 border-b border-slate-800 sticky top-0 z-40 px-6 py-4 flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <span class="text-xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-sky-400 to-indigo-500">Jerry Yang · Playbook Portal</span>
            <span class="bg-sky-500/10 text-sky-400 text-xs px-2.5 py-1 rounded-full font-semibold border border-sky-500/20">CI Action Flow Page</span>
        </div>
        <div class="flex items-center space-x-4">
            <a href="index.html" class="text-sm text-slate-400 hover:text-white transition-colors">📄 Welcome Dashboard</a>
            <span class="text-slate-700">|</span>
            <span class="text-xs text-slate-500 font-mono">Status: Secure Sandbox Active</span>
        </div>
    </header>

    <div class="flex flex-1 overflow-hidden">
        <!-- Persistent Sidebar -->
        <aside class="w-80 bg-slate-900 border-r border-slate-800 p-6 overflow-y-auto hidden md:block">
            <!-- Sidebar search -->
            <div class="mb-6">
                <input type="text" id="docSearch" placeholder="搜尋筆記..." class="w-full bg-slate-800 border border-slate-700 rounded-md px-3 py-2 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-sky-500" />
            </div>
            
            <nav class="space-y-6" id="sidebarNav">
                {sidebar_html}
            </nav>
        </aside>

        <!-- Main Content Pane -->
        <main class="flex-1 overflow-y-auto p-8 md:p-12 lg:p-16 max-w-5xl mx-auto w-full">
            <div class="markdown-body">
                {body}
            </div>
        </main>
    </div>

    <!-- Prism.js Scripts for Code Highlighting -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-core.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
    
    <!-- Inline Search Script -->
    <script>
        document.getElementById('docSearch').addEventListener('input', function(e) {{
            const query = e.target.value.toLowerCase();
            const categories = document.querySelectorAll('#sidebarNav > div');
            
            categories.forEach(cat => {{
                let catMatches = 0;
                const items = cat.querySelectorAll('li');
                
                items.forEach(item => {{
                    const text = item.textContent.toLowerCase();
                    if (text.includes(query)) {{
                        item.style.display = 'block';
                        catMatches++;
                    }} else {{
                        item.style.display = 'none';
                    }}
                }});
                
                if (catMatches > 0 || query === '') {{
                    cat.style.display = 'block';
                }} else {{
                    cat.style.display = 'none';
                }}
            }});
        }});
    </script>
</body>
</html>"""

def get_welcome_page(categories):
    sidebar_html = ""
    for cat, items in sorted(categories.items()):
        sidebar_html += f'<div class="mb-4"><h3 class="text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">{cat}</h3><ul class="space-y-1">'
        for item in items:
            sidebar_html += f'<li><a href="{item["url"]}" class="block px-3 py-1.5 rounded-md text-sm transition-colors text-slate-300 hover:bg-slate-700 hover:text-white">{item["title"]}</a></li>'
        sidebar_html += '</ul></div>'

    dashboard_cards = ""
    for cat, items in sorted(categories.items()):
        dashboard_cards += f"""
        <div class="bg-slate-900 border border-slate-800 rounded-xl p-6 hover:border-sky-500/50 transition-all duration-300">
            <h3 class="text-lg font-bold text-sky-400 mb-3 flex items-center justify-between">
                <span>📂 {cat}</span>
                <span class="bg-sky-500/10 text-sky-400 text-xs px-2.5 py-0.5 rounded-full font-semibold border border-sky-500/20">{len(items)} 篇</span>
            </h3>
            <ul class="space-y-2.5">
        """
        for item in items[:4]:  # Show up to 4 items in each card
            dashboard_cards += f'<li><a href="{item["url"]}" class="text-sm text-slate-300 hover:text-white hover:underline transition-all flex items-center space-x-2"><span>📄</span> <span class="truncate">{item["title"]}</span></a></li>'
        if len(items) > 4:
            dashboard_cards += f'<li class="pt-2"><span class="text-xs text-slate-500 italic">還有更多篇...</span></li>'
        dashboard_cards += "</ul></div>"

    return f"""<!DOCTYPE html>
<html lang="zh-TW" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard | Jerry's Growth Docs</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        slate: {{
                            950: '#0b1329'
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        ::-webkit-scrollbar {{
            width: 6px;
            height: 6px;
        }}
        ::-webkit-scrollbar-track {{
            background: #1e293b;
        }}
        ::-webkit-scrollbar-thumb {{
            background: #475569;
            border-radius: 3px;
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col font-sans">
    <!-- Top Navbar -->
    <header class="bg-slate-900 border-b border-slate-800 sticky top-0 z-40 px-6 py-4 flex items-center justify-between">
        <div class="flex items-center space-x-3">
            <span class="text-xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-sky-400 to-indigo-500">Jerry Yang · Playbook Portal</span>
            <span class="bg-sky-500/10 text-sky-400 text-xs px-2.5 py-1 rounded-full font-semibold border border-sky-500/20">CI Action Flow Page</span>
        </div>
        <div class="flex items-center space-x-4">
            <span class="text-xs text-slate-500 font-mono">Status: Secure Sandbox Active</span>
        </div>
    </header>

    <div class="flex flex-1 overflow-hidden">
        <!-- Persistent Sidebar -->
        <aside class="w-80 bg-slate-900 border-r border-slate-800 p-6 overflow-y-auto hidden md:block">
            <!-- Sidebar search -->
            <div class="mb-6">
                <input type="text" id="docSearch" placeholder="搜尋筆記..." class="w-full bg-slate-800 border border-slate-700 rounded-md px-3 py-2 text-sm text-slate-200 placeholder-slate-500 focus:outline-none focus:border-sky-500" />
            </div>
            
            <nav class="space-y-6" id="sidebarNav">
                {sidebar_html}
            </nav>
        </aside>

        <!-- Main Content Dashboard -->
        <main class="flex-1 overflow-y-auto p-8 md:p-12 lg:p-16 max-w-6xl mx-auto w-full">
            <div class="mb-10 text-center md:text-left">
                <h1 class="text-4xl font-extrabold text-white mb-3">歡迎來到您的個人資安與技術成長手冊 🚀</h1>
                <p class="text-slate-400 text-lg max-w-3xl leading-relaxed">此系統已成功將您過去 3 年在邊信聯科技 (FiduciaEdge) 積累的 3,200 多行 TPM 硬體信任根、Secure Boot 與代碼簽章沙盒等高難度實戰筆記重構為結構化、模組化的文檔庫。歡迎閱讀和 review 您所累積的技術財富。</p>
            </div>

            <!-- Dashboard Cards Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-12">
                {dashboard_cards}
            </div>

            <!-- Quick Access Focus Callout -->
            <div class="bg-gradient-to-r from-slate-900 via-sky-950/40 to-slate-900 border border-sky-500/20 rounded-xl p-8 flex flex-col md:flex-row items-center justify-between">
                <div class="mb-6 md:mb-0 md:mr-8 text-center md:text-left">
                    <h2 class="text-xl font-bold text-sky-400 mb-2">⭐ 技術回顧必讀：3 年技術成就總結與能力展望</h2>
                    <p class="text-slate-300 text-sm leading-relaxed max-w-2xl">我們已經為您特別撰寫了一份完整的資深資訊安全工程師職能回顧。這將幫助您梳理自己在 TPM 身分識別、雙向憑證沙盒以及機密邊緣容器部署上的成果與國際級大廠（如 Google 安全團隊）的能力對齊。</p>
                </div>
                <a href="domains_05-security-trusted-systems_portfolio-summary.html" class="bg-sky-600 hover:bg-sky-500 text-white font-semibold text-sm px-6 py-3 rounded-lg shadow-lg hover:shadow-sky-500/20 transition-all duration-300 flex items-center space-x-2 whitespace-nowrap">
                    <span>閱讀成就總結</span>
                    <span>➔</span>
                </a>
            </div>
        </main>
    </div>

    <!-- Inline Search Script -->
    <script>
        document.getElementById('docSearch').addEventListener('input', function(e) {{
            const query = e.target.value.toLowerCase();
            const categories = document.querySelectorAll('#sidebarNav > div');
            
            categories.forEach(cat => {{
                let catMatches = 0;
                const items = cat.querySelectorAll('li');
                
                items.forEach(item => {{
                    const text = item.textContent.toLowerCase();
                    if (text.includes(query)) {{
                        item.style.display = 'block';
                        catMatches++;
                    }} else {{
                        item.style.display = 'none';
                    }}
                }});
                
                if (catMatches > 0 || query === '') {{
                    cat.style.display = 'block';
                }} else {{
                    cat.style.display = 'none';
                }}
            }});
        }});
    </script>
</body>
</html>"""

if __name__ == "__main__":
    build_docs()
