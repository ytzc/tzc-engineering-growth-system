# Miscellaneous Security Notes

# 11/28
* CIAAC
```
邊信聯科技股份有限公司 (台北辦公室)
FiduciaEdge Technologies Co., Ltd. (Taipei office)
楊子擎 Jerry  Yang
jerry.yang@fiduciaedge.com
 +886 966 765 256
(03) 668-7008 分機304
軟體工程師
software engineer 
105台北市松山區南京東路四段2號3樓 (台灣科技新創基地)
(Taiwan Tech Arena ) 3F., No. 2, Sec. 4, Nanjing E. Rd., Songshan Dist., Taipei City 105, Taiwan (R.O.C.) 
 
(中文) https://fiduciaedge.com/zh/home-tw/
(English) https://fiduciaedge.com/

```

# 11/14
## 10/21
* livenessprobe
* create wait 1s
* file api
## 10/18
* todo 
    * unauth-cluster issue
    * pre-install and uninstall for  helm-chart to setup ippool
    * test network policy
    * test script for fECB-API (mTLS)

# 10/11



## 10/4
* meeting
    * test-pod
    * job -> daemonset -> mount
    * ota-api
    * file-api
        * 沒用的刪掉
    * 自動掛載
        * system-api
```
cp fecb-supplements/fecb-system-api/fecb-system-api.service /etc/systemd/system


```
### test-pod
* system
* vault
* fecb
* agent

# 9/19
## 9/15
* 統一變數mtls
    * Fix mtls environment variables to follow naming convention
# 9/12
## 9/11
# 9/5
## 9/5
* device-api path append
    * 
## 8/30
* capability bug

# 8/29
# 8/22


## 8/22
* create capability, create device
    * capability不見
## 8/19
* ota-api
* pod db
## 8/15
* configure mender
    * cli call
    * mender configure

# 8/8
https://hackmd.io/@lorex8711/fhir-server

## 8/11
* Debian image configure
## 8/7
* mender
    * 2
    * 3
    * 6
* Artifact
    * Update Modules被end user影響
        * authorized_keys file to the /home/${USER}/.ssh
    * 下載script(single file Update Module)
        * https://github.com/mendersoftware/mender/blob/3.5.1/support/modules/single-file
    * 產生mender artifact ->module-image (.mender)
    * 寫update module
        * https://github.com/mendersoftware/mender/blob/3.5.1/Documentation/update-modules-v3-file-api.md
    * 
    * UI Create a deployment
    * mender-cli 檢查
* Create-a-custom-update-module
    * update module
        * https://hub.mender.io/c/update-modules/13****
    * file-api
        * https://github.com/mendersoftware/mender/blob/master/Documentation/update-modules-v3-file-api.md#file-api
    * stream
        * https://github.com/mendersoftware/mender/blob/master/Documentation/update-modules-v3-file-api.md#streams-tree
    * flow
        * device update module
            * /usr/share/mender/modules/v3 放script
        * server
            * mender-artifac 創造 Mender Artifact(module-image)
        * device
            * Standalone Mode mender install xxx.mender
        * Rollback/power loss


## 7/28
* tiip meeting
    * 3
        * review上一次
* encryption
    * gpg smine mender
# 7/25
* 書 rust 權威指南,數位憑證技術與應用
fiducia@192.168.20.67
* overview whole picture

## 7/24
* mtls
    * notfound errorcode 做好
        * box指針
    * 等system timeout 做好
    * disable option 做好
    * health check 做好
        * tonic_health
        *  tonic_health::pb::health_client::HealthClient;
    * trait util (TLS struct)
    * test.rs
    * 修改metadata
    * health check not serving機制


https://github.com/hyperium/tonic/blob/master/examples/src/health/server.rs
https://github.com/grpc/grpc/blob/master/doc/health-checking.md
## 7/20
* 
## 7/18
* mTLS
* mariadb pod


## 7/19
* 整理rust
* trait 了解james問題
* openpgp

## 7/20
* 重寫fileapi
    * mariadb
    * mtls
    * helm chart

# 7/18
## 7/13
v
* 投影片動畫
    * tuf
    * notary
    * 攻防
    * trivy
* 完成攻防影片 文件
* 修改測試報告
* 補充使用手冊
## 7/12
* 投影片動畫
    * tuf
    * notary
    * 攻防
* 錄製攻防影片
* 寫攻防文件
* 修改測試報告
* 補充使用手冊
## 7/11
* 錄製攻防影片
* 寫攻防文件
* 修改測試報告
* 補充使用手冊


# 7/11
* TUF架構
* Apache, nginx

## 7/10
* 攻防情境文件, 影片
* 測試報告調整
* 使用手冊補充
* TUF架構
* Apache, nginx架構了解


## 7/9
* 攻防情境文件, 影片
## 7/7



```

echo "check database token EXIST: "
sqlite3 /opt/fiducia/db/edge.db "SELECT CapabilityToken  FROM capability where servicename=\"init-selector\";"

echo "check capability api LOG: "
capability-POD="$(sudo kubectl -n fecb-system get pod --field-selector spec.nodeName=$HOSTNAME --no-headers | awk '{print $1}' | grep capability)"
sudo kubectl logs -n fecb-system $capability-POD | tail -n 20
echo "END capability api LOG: "
```
# 7/4
* static build system api
* 了解 "ingress", "clusterIP", "nodePort" or "loadBalancer"
# 6/27
## 6/12
### capability
* 單獨create, delete capability(dvc) 50次
    * debug6.sh
        * 第28,10次錯
        * create等很久
            * 找到pod_name
            * 看不到pod phase/ip
            * 發現從pod name就錯了
            * 卡住無窮迴圈
* 單獨create, delete capability(dvc) 50次 去掉等待測試
    * 43次錯誤
    * 幾乎都沒插入podip
    * pod name等到同一個
    * 解法
        * 創造不同的selector
        * 取得最新的pod name
            * 依照timestamp
            * 陣列

* 一個teminating,一個init
    * debug7.sh
```

sudo kubectl get deployment -l app=app-selector -o jsonpath='{.items[0].metadata.name}'

sudo kubectl get pod -l app=app-selector -n default --no-headers | wc -l


sudo kubectl get pod -l app=app-selector -n default -o jsonpath='{.items}'






sudo kubectl get pod -l app=app-selector -n default

sudo kubectl get pod -l app=app-selector -n default -o jsonpath='{.items[0].metadata.name}'


sudo kubectl get pod -l app=app-selector -n default -o go-template='{{printf "%d\n" (len  .items)}}'
```

* annotation 實作cleanup
    * debug9.sh
* 測試拿最新pod 
    * dubug19.sh
* 問題 terminating的db要不要刪掉
## 6/10
* rust程式設計
    *  trait
    *  async
        *  concurrency
        *  parallelism
## 6/9


### check function
https://blog.pan93.com/what-is-rust-async/
#### probe
* 檢查pod被刪除 
* device run
    * 測試grpc
    * 執行刪除
# 6/6
* argoCD
* openshift
* PostgreSQL 
* go
* tls/ssl 網路架構
* traefik

## 6/6
* get pod name
```
sudo kubectl get pods -l app=app-py -n default -o jsonpath='{.items[0].metadata.name}'

sudo kubectl get pods app-svc


sudo kubectl describe svc app-svc -o json
sudo kubectl get svc app-svc -o json
sudo kubectl get svc app-svc -o jsonpath='{.metadata.labels}'
```
## 6/3
* git lab push
```
fatal: unable to access 'https://gitlab.fiduciaedge.work/sys-dev/fecb-capability-api.git/': Failed to connect to gitlab.fiduciaedge.work port 443: No route to host
```
* json parser
```
{\"HC\":[],\"DEVICE\":[{\"service_ip\":\"172.47.145.186\",\"name_ports\":\"p1:9000,p2:9001\"}]}
```

```
{"HC":[],"DEVICE":[{"service_ip":"172.47.145.186","name_ports":"p1:9000,p2:9001"}]}
```
### 收尾
* init
    * get secret
    * api -> sdk
* gitlab/capability/util/get_pods_name
    * 改成使用svc name
    * 去掉-l arg_servicename
* file 
    * get ver
### todo

* gitlab/fecb-client-aou-sample-code/python/src/init
    * 完成init.sh
        * 移除跳脫字元
        * 格式svc_name,svc_ip,name_ports (get svc)

    * parse json
        * device
            * name, ip, nameports
    * get secret
    * error code
    * api -> sdk

## 6/2
* gitlab/fecb-client-sdk-sample-code/python/src/init
    * 完成init.sh
    * parse json
* gitlab/capability/util/get_pods_name
    * 改成使用svc name
    * 去掉-l arg_servicename
* gitlab/file
    * getver
* gitlab/fecb-client-sdk-sample-code/python/src/init
    * secret 部屬secret方式
* gitlab/system
    * getver
* 改用manefist滿足不同平台

## 6/1
* getservice
* init script


## 5/30
* argoCD
* openshift
* PostgreSQL 
* go
https://kubeoperator.io/docs/user_manual/argocd/
# 5/30


# 5/23
### todo
* 了解htop看系統資源
* 

## 5/21
* secrete/ selector

* 攻防情境
* init
* manifest

### todo
* 寫自己的helm chart
* secret selector
* notary server設定完成
## 5/19
* 了解notary-secret.yaml
* 放置uca.crt
# 5/16

### 

## 5/12
* v1.4.2
    * file
    * capability
    * dvc
    * hc
    * demo (todo)
* v1.4.3
    * file
        * upload file encrypt(todo)
    * capability
        * get svc
    * dvc
        * new dvc
        * error code
    * hc
        * new hc
        * error code
    * demo
# 5/9


## 5/9

* code
    * new dvc
    * new hc
    * get svc
    * init.sh




* getsvc all
* PlantUML

* sequence diagram




## 5/7
# 5/2

# 4/25
# 4/18
# 4/11
## 4/9
~1 寫3,4
~2 佈署 3 4
~3 寫5,1
https://blog.51cto.com/lidabai/5195706
https://helm.sh/zh/docs/intro/using_helm/
https://ithelp.ithome.com.tw/articles/10301191


# 2/21
# 2/14
# 2/7

# 1/31
# 1/19
* video POS
* 測試
# 1/31
## note
* kubernete
* leetcode
* 隱私計算

# 1/17
* arm fecb
    * file
    * hc
    * capability
    * device
    * system 
    * agent
* minio trafix 443, 30189


# 1/10
# 12/26
# 12/20
# 12/12
## 12/6
### notary




# 12/5
## 12/5
* ~1200 grpc api
* ~1300 fusing server
## 12/3
### key host

## 11/28
* 8221
* restful
* gitlab
## 11/30
* TAA
* 17:00開會

# 11/8
# 10/24
* rust 書 

# 10/17
# 10/10
# 10/3
### Meeting
* secure storage (device) key 沒有切割使用者帳戶
* email encryption (user) key使用者帳戶
* secure file transfer

# 9/26
## 9/21
# 9/19
## 9/14
* API test ~16
    * local測試完
    * pod設計
* 6450 ~18
* rust service ~20
* 交通費
## 9/13
* API test ~9
    * local測試完
    * pod設計
* 6450 ~10
* rust service
## 9/12
* API test
* python code
# 9/12
### progress
* test pod
    * python
### Note

* godaddy
    * 域名註冊 fiduciaedge.work 買網站
## 9/9
* 解決gitlab


### 讀書筆記 數位憑證技術與應用


## portainer note

1 選取device node進行設置
2 file server透過machine key部屬檔案
```
fiduciaedge/fecb-java-sdk:v1.4.0-x86


command: [ "/bin/sh"] #, "setup.sh" ]
args: ["-c", "while true; do echo hello; sleep 10;done"]
env:
- name: NETWORK_INTERFACE
  value: "172.3.0.1:"
```

* 查詢capability
```

```
# 8/22
