import os
import re

def split_notes():
    input_path = "domains/05-security-trusted-systems/tpm整理筆記.md"
    output_dir = "domains/05-security-trusted-systems/archive"
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(input_path):
        print(f"Input file not found: {input_path}")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # We will split the file by H1 and H2 headers that look like dates or titles
    # A header starts with # or ## or ###
    blocks = []
    current_block = {"header": "Intro", "lines": []}
    
    header_pattern = re.compile(r"^#+\s+(.*)")

    for line in lines:
        match = header_pattern.match(line)
        if match:
            if current_block["lines"]:
                blocks.append(current_block)
            current_block = {"header": match.group(1).strip(), "lines": [line]}
        else:
            current_block["lines"].append(line)
            
    if current_block["lines"]:
        blocks.append(current_block)

    # Output categories
    categories = {
        "tpm-key-provisioning.md": ["tpm", "idevid", "ldevid", "credential", "aik", "duplicate", "import", "pkcs11", "ek", "cert"],
        "secure-boot-infosec.md": ["secure boot", "mok", "fuse", "jetson", "kernel", "boot", "tegra", "grub", "l4t"],
        "twca-code-signing-sandbox.md": ["twca", "sign", "hash", "verify", "p7", "signtool", "hashtool", "verifytool", "cryptotool"],
        "container-sandbox-fecp.md": ["container", "fecp", "cosnar", "ccsaas", "spire", "spiffe", "docker", "kubernetes", "k8s", "sandbox", "pistis", "harbor"]
    }

    # Initialize files with headers
    files_content = {cat_file: ["# " + cat_file.replace(".md", "").replace("-", " ").title() + "\n\n"] for cat_file in categories}
    files_content["misc-notes.md"] = ["# Miscellaneous Security Notes\n\n"]

    for block in blocks:
        block_text = "".join(block["lines"]).lower()
        matched_category = None
        max_matches = 0

        # Find the category with the most keyword matches
        for cat_file, keywords in categories.items():
            matches = sum(1 for kw in keywords if kw in block_text)
            if matches > max_matches:
                max_matches = matches
                matched_category = cat_file
        
        if max_matches > 0 and matched_category:
            files_content[matched_category].extend(block["lines"])
        else:
            files_content["misc-notes.md"].extend(block["lines"])

    # Write the files
    for cat_file, content_lines in files_content.items():
        # Only write if there's actual content (more than just the header)
        if len(content_lines) > 1:
            out_path = os.path.join(output_dir, cat_file)
            with open(out_path, "w", encoding="utf-8") as out_f:
                out_f.writelines(content_lines)
            print(f"Wrote {len(content_lines)} lines to {out_path}")

if __name__ == "__main__":
    split_notes()
