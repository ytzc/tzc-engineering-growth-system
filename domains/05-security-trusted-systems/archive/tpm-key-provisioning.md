# Tpm Key Provisioning

Weekly progress 2
===
## 11/29
* activate credential
    * device ID
    * credential resp
        * encCert
        * secret
        * encIdentity
        * identityHmac
        * cn
* 使用IDevID對PC 進行遠程配置
    * 目標
        * 產生簽名key IDevID發起VPM連接
* 步驟
    * EK產生受限制的簽名key 只有對應EK可以導入
    * 
* Tray meeting
```
技术1详细步骤：
创建TPM中可复制的、有策略的限制签名密钥。
使用企业CA为该密钥生成证书，验证EK证书的有效性。
使用TPM2_Duplicate命令将密钥复制为三个文件：TPM2B_PUBLIC、TPM2B_PRIVATE、加密值（允许具有正确EK的TPM重新生成种子）。
将这三个文件发送到目标PC。
在目标PC上，如果EK不存在，使用TPM2_CreatePrimary重新生成EK。
使用TPM2_Import命令，将三个文件导入目标PC的TPM。
当EK在TPM中时，使用TPM2_Load命令加载IDevID密钥。
技术2详细步骤：
在TPM外部创建IDevID，无需与TPM关联策略。
创建三个文件，包含IDevID的公共数据、私有数据（使用AES加密），以及允许具有EK的TPM计算出种子的加密值。
将这三个文件发送到目标PC。
在目标PC上，使用TPM2_Import命令将这三个文件导入TPM。
技术3详细步骤：
在TPM外部生成IDevID的公共数据，并创建允许复制的策略。
使用TPM2_LoadExternal命令将IDevID导入TPM。
在目标PC上，加载EK的公共部分，满足复制策略，复制IDevID密钥生成三个文件。
将这三个文件发送到目标PC。
在目标PC上，使用TPM2_Import命令将这三个文件导入TPM。
```
### provision key deviceID
* 原本是產生pfx pkcs12 給客戶 用密碼解開 存放在某個地方
* tpm2.0 IDevID
    * EK產生受限制的簽名key 只有對應EK可以導入
* 創建IDevID技術
#### 技術1： duplicating the key, parent is the EK.
* 在伺服器端的TPM或TPM模擬器中建立IDevID，並使用標準CA為其建立憑證。
* 複製金鑰，以便能夠將其匯入具有客戶端EK的系統中。

##### 詳細步驟
* 創建可複製的, 有策略的, 限制簽名key 
    * TPM2_Create AIK (deviceID)
    * 策略
        * TPM2_polictCommandCode, TPM2_Duplicate 要限制只有對應EK
        * TPM2_PolicyDuplicateSelect 只要把父密鑰設為EK公鑰
* 頒發證書，對IDevID生成證書，證書的過展中添加EK信息 EK pub key
* 密鑰複製
    * TPM2_Duplicate
        * TPM2B_Public pubkey
        * TPM2B_Private 被對稱加密prikey, pubkey binding HMAC
        * encrypted value

#### 技術2：
* 建立IDevID並對其進行簽名。
* 封裝它，使其看起來像是可複製的TPM金鑰，可以匯入到客戶端的EK中。

#### 技術3：
* 建立IDevID並對其進行簽名。
* 在本地TPM或TPM模擬器中將其導入，然後複製以使其新的父級是客戶端TPM的EK。
# 11/7
* helm-chart
* init
    * init (need getfile from fECP Tools)
    * tls-bootstrap
* workerNode
    * ca-bundle-injector
    * copysystem(need system-api from XXX Tools)
* hooks-job
    * calico-job
* hooks-test
    * testpod
* monitor
    * checker

* helm-chart
    * init
        * init (need getfile from fECP Tools)
        * tla-bootstrap
    * workerNode
        * ca-bundle-injector
        * copysystem(need system-api from XXX Tools)
    * hooks-job
        * calico-job
        * tls-bootstrap
    * hooks-test
        * testpod
        * checker


core

HC
Device
OTA
System
File
Capability


ui

fECB Agent
Portainer fECB


e2ee

Cert Agent
Cert Wardan (need uplader from fECP Tools)
# 10/31
```
init-657658c779-zxgfq
init-657658c779-zxgfq

export POD=init-657658c779-zxgfq
export FECB_CAPABILITY_API_SERVER_URL="172.3.0.1:30891"
kubectl exec -it $POD -- ./grpcurl --key /tls/client/tls.key --cert /tls/client/tls.crt -cacert /tls/server/ca.crt  -import-path ./proto -proto capability-api.proto $FECB_CAPABILITY_API_SERVER_URL capability.CapabilityService/GetToken 



```

* testpod v1.4.5-test
    * ok
* init v1.5.0
    * ok
* ca-bundle-injector:v1.0.0
    * ok
* checker v0.1.0-test
    * ok
* fecb api v1.5.0
    * ok
* fecb-tls-bootstrap v1.0.0
    * ok
* calico-job v1.0.0
    * ok
* fecb-system-api-bootstrap v1.0.0
    * ok

* init
* ca
* calico
* checker
* copy file
* api

```
 ERROR fecb_file_api::utils     > "gpgsm: failed to create temporary file '/opt/fiducia/.gnupg/.#lk0x00005599df4ecc80.fecb-file-api-mjqt7.155107': No such file or directory\ngpgsm: keyblock resource '/opt/fiducia/.gnupg/pubring.kbx': General error\n"
```
restart 解決
```
curl -X POST "$MENDER_SERVER_URI/api/management/v1/deployments/deployments" \
      -H "Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI1NmVjZmVhNC0zYmNjLTQ0NTktODM4ZS1hNWNmMWZjMTQ0YzYiLCJzdWIiOiIyNWRmM2UyMy0zYWU5LTRjYTItYTNmNi01MjAzODU1Njg2ZjEiLCJleHAiOjE2OTkyNzMwMTQsImlhdCI6MTY5ODY2ODIxNCwibWVuZGVyLnVzZXIiOnRydWUsImlzcyI6Ik1lbmRlciBVc2VycyIsInNjcCI6Im1lbmRlci4qIiwibmJmIjoxNjk4NjY4MjE0fQ.ixXepA_YPKALJNVdx1SUM-FGZ5fDrHQHSTZ0wXVyBLRgVSrSS3Fumx0E0ZeAZEacaLDf3S7IQP4HVbcqW-gKN_d6tfyyoteMOzwlzB3DK6xyzUFIzLC8UG5Trsmz04vTEeOXo8IhQE3JUt-Hhn5tvwrxjSiN1-HDuwCZYkSZlJvZWyio3S34ZXPoS_I8d_EH15sUHW_UqmtxARs5Lp6-8lm4TJ2g52oDeqz8oUxp-lZreWlq5i2IM6ydI_yLmiAlhkGG8B1YL16WmznpLOQd6hCvY47P3ZgW8OEp6i4rT7RKW68ia51GqFCSNDtGowIWiJAM0tHxOGtKRitstKHbEg" \
      -H "Content-Type: application/json" \
      -d "{
          \"name\": \"testfile2.cms\",
          \"artifact_name\": \"testfile2.cms\",
          \"all_devices\": true
      }"
```


* 10.133 uploader
./fe-upload upload test -r $FE_UPLOAD_RECIPIENT_ID
gpgsm --list-key |grep aka
./fe-upload list-pkcs
```
./grpcurl --key /tls/client/tls.key --cert /tls/client/tls.crt -cacert /tls/server/ca.crt -import-path ./proto -proto capability-api.proto $FECB_CAPABILITY_API_SERVER_URL capability.CapabilityService/GetToken
```
./grpcurl --key $CLIENT_KEY --cert $CLIENT_CERT -cacert $SERVER_CERT_CA -import-path ./proto -proto capability-api.proto $FECB_CAPABILITY_API_SERVER_URL capability.CapabilityService/GetVer

* apply hc
    * svc不給 new hc要卡住
kubectl get pod -l app=init-pod -n default --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[0].metadata.name}'

10.133
tmux 0 uploader
# 10/17
* cert 27001
* Horizontal Pod Autoscaler(節點異常)
    * 增加pod資源
    * 提高穩定性與成本節約
    * 避免節點異常
* 水平擴展
    * GPU training
    * 平行增加pod數量
* Priority and Preemption(服務異常)
    * 關閉低優先權的服務，確保核心服務持續運作
* Disruption Budget
    * 保護應用避免因中斷而損壞
* Threat matrix for Kubernetes



## 10/12
* mtls system-api
* reload整理
* file-api
* ota-api
* db重新架設
* system-api轉成pod
* twca meeting
    * a1金要登陸平台
        * 11月中
        * tpm tool取出EK 公鑰 憑證
    * a2 
        * IdevID
        * remote attestation 

## 10/5
* todo
    * fecb自己
        * readness看system-api
        * liveness看自己
    * testpod: fecb-health
        * liveness 看fecb restart
        * readness 看system api
    * fileapi整理
    * 整理gary
    * reload
* system-api啟動才通過fecb probe
    * system-api沒啟動, health顯示失敗, pod等待重新啟動
    * system-api重啟, pod重新啟動成功
    * system-api stop, fecb重啟動
* file-api

* test-pod
    * 確認每一個fecb

* init-container
    * test-vault
* cert變動 reload
* * readinessProbe
    * system有才ready
* liveness
    * cert reload

* todo
    * test-fecb-pod
* liveness reload
# 10/3
fecb-system-api-fecp-worker-client-cert-tls
fecb-system-api-fecp-worker-server-cert-tls
* system-api

* meeting
    * test-pod
    * job -> daemonset -> mount
    * ota-api

    * file-api
        * 沒用的刪掉

## 10/2

* fecb cert mount
    * 討論改成自動取消
* init-container
    * 加上csi mtls
* test-api
    * pod 寫進helm chart確保api 都跑起來
* proto 放進pod
* gary meeting
    * fileapi 
        * 刪除minio alias

    * fecb cert mount
        * 改成daemonset
        * hostname issue?
            * 每一個node都用同一個tls cert, 不走hostname

    * init-container
        * 加上csi mtls
    * test-api
        * pod 寫進helm chart確保api 都跑起來
    * ota-api
        * 先跑230
        * configure測試
    * 有時間再做
        * reload secret
            * 怕來不及 有時間再做
        * system pod lifecycle
            * 先不做 很多要設計

## 9/27
* 202 204 207 208 209 
    * 202 
    * 204
        * 完成
    * 207
        * 沒驗證
    * 208
        * 做完
    * 209
        * 做完
* cert發布
* ns創建
* cert reloader
* ota-api
* gary meeting
    * fileapi 
        * 刪除minio alias

    * fecb cert mount
        * 改成daemonset
        * hostname issue?
            * 每一個node都用同一個tls cert, 不走hostname

    * init-container
        * 加上csi mtls
    * test-api
        * pod 寫進helm chart確保api 都跑起來
    * ota-api
        * 先跑230
        * configure測試
    * 有時間再做
        * reload secret
            * 怕來不及 有時間再做
        * system pod lifecycle
            * 先不做 很多要設計

### j204
* cert
    * fecb-system-api-fecp-worker
## 9/26
* todo
    * 202 204 207 208 209 
    * agent改寫
    * health-check
        * 連通 
    * cert發布
    * cert reloader
    * ota-api
# 9/26
* cert誰發
* ns誰創
    * 我來做


* 9/22
    * /manifests/fecb/fecb-api-system-deployment.yaml"
    * ./manifests/fecb/fecb-agent-deployment.yaml



Ask for one day leave on 9/22
```
Dear John,

I am writing this letter to apply my 生日假 for taking one day leave on 9/22(Friday), 
kindly please approve.

Best Regards,
Jerry

```
## 9/18
* constant.rs
    * 設定變數名稱
    * 預設字串
* util
    * watch_service_status
    * check_system
    * db_operation
        * identity

```
use crate::SERVER_CERT_PATH;
use crate::SERVER_KEY_PATH;
use crate::CLIENT_CA_CERT_PATH;
use crate::SYSTEM_CLIENT_CERT_PATH;
use crate::SYSTEM_CLIENT_KEY_PATH;
use crate::SYSTEM_SERVER_CA_CERT_PATH;


    let identity = Identities{
        server_cert_path:(*SERVER_CERT_PATH).lock().unwrap().clone(),
        server_key_path:(*SERVER_KEY_PATH).lock().unwrap().clone(),
        client_ca_cert_path:(*CLIENT_CA_CERT_PATH).lock().unwrap().clone(),
        system_client_cert_path:(*SYSTEM_CLIENT_CERT_PATH).lock().unwrap().clone(),
        system_client_key_path:(*SYSTEM_CLIENT_KEY_PATH).lock().unwrap().clone(),
        system_server_ca_cert_path:(*SYSTEM_SERVER_CA_CERT_PATH).lock().unwrap().clone(),
    };
    let channel = Channel::from_static(FECB_SYSTEM_API_SERVER_URL.as_str())
        .tls_config(identity.client_system_mtls().await)
        .unwrap()
        .connect()
        .await
        .unwrap();
```
* 修正順序
    * capability
    * file
    * device
    * hc
* watch
## 9/10
* watch看到cert被改動要重新啟動
* mariadb pod lifecycle
* system api去access database api
* helm chart
## 8/16
* meeting
    * ota update
    * kubernetes
    * 身分認證代理程式
        * 不在sandbox 在remote attestation(TPM)
        * 軍方定義ID中心
    * feature
        * 設備身分
            * DEVICE cert sandbox(fECB)
        * 可信軟體模組
            * fECB
        * 可信資料交換
            * file api
        * 可信晶片供應商
            * TPM　API
* todo
    * tiip錄影
    * demo script
    * tpm remote attestation ppt
    * file api
        * 去除.csm
    * ota api
# 8/1
* 書:Rust權威指南, linux shell, kubernetes
* 書rust程式設計
* 書~20章
* vault, minio, cert manager, pfsence routing
* todo
    * Kubernetes 
    * minio
    * mTLS
    * mender
## 7/26
* bug fix
    * fiducia@192.168.20.67
* file api
    * configure minio errorcode

```
kubectl -n vault exec vault-0 -- vault kv get kv/admin-credentials/fecb-file-server/minio/access-key | awk 'END {print $2}'

* Vault is sealed
command terminated with exit code 2
```


* minio access
```

```

* mTLS整合完畢
    * 書~16章
    * tune code
    * test.rs
* gitlab 
    * mearge
    * squash
* overview whole picture
    * error code(health check)

## 7/25
* system api
    * utils::set_kube_path();
    * renew certificate
* capability
    * utils::set_kube_path(); 
* bug fix
    * fiducia@192.168.20.67

## 7/25
* mtls

* health check
    * check identity ok
    * check system ok
* 實作每個API
    * secret cert
    * readness probe
* clean up
* init container
* fix bug

## 7/6
* docker login hostname issue
* k3s deploy cert issue


### todo


* system 
    * getver
    * pooling
        * 刪除pod
            * 刪除capability
            * 刪除resource
* info改成debug
* capability
    * list(app,hc,dvc)要修改前贅詞
    * create capability pod ip會找不到
        * 確認podip存在才寫入
        * 確認不是terminating 等待
* file
    * checksum
    * upload
    * checksum
    * prefetch

* fecb api pod cert 改變就要重新抓cert


* info改成debug
* file api
    * host alias 192.168.10.231
    * hostname
## 6/8
* capability
    * list(app,hc,dvc)要修改前贅詞
    * create capability pod ip會找不到
        * 確認podip存在才寫入
        * 確認不是terminating 等待
* file
    * checksum
    * upload
    * checksum
    * prefetch

* fecb api pod cert 改變就要重新抓cert

* system 
    * getver
    * pooling
        * 刪除pod -> 刪除capability
* info改成debug
* file api
    * host alias 192.168.10.231
    * hostname
## 6/7
* system
    * ListVirtualDevice
* file
    * checksum
    * upload
    * checksum
    * prefetch
* list hc bug
    * db:image_name ->要修改所有protobuff
* 重複動作error code
* capability
    * list(app,hc,dvc)要修改前贅詞
    * create capability pod ip會找不到
* fecb api pod cert 改變就要重新抓cert

* system 
    * getver
    * pooling
        * 刪除pod -> 刪除capability
## 6/6
* system 
    * getver
    * pooling
        * 刪除pod -> 刪除capability


* tiip
```
https://192.168.31.5
```



```
./grpcurl  -cacert /opt/client/tls/ca-cert.pem  -import-path ./proto -proto capability-api.proto $FECB_CAPABILITY_API_SERVER_URL capability.CapabilityService/GetToken | jq .userToken)

```
## 6/5
* init 
    * cert secret
    * selector 改成svc
    * 整理git lab
* system 
    * getver
    * pooling
        * 刪除pod -> 刪除capability
### muti svc


* new devie
    * get_service_ip_from_svcname
    * get_service_port_from_profile
    * profilename 要對到port的name
    * new device data
        * ProfileName
        * AssociateResourceSandboxName
        * DeviceLocation
        * DataType
        * InteractionMode
        * DeviceType
        * ProxyUUID
        * ServiceLocation
        
```
kubectl get svc device-service-py -o jsonpath='{.spec.ports}' -n resource-sandbox

kubectl get svc device-service-py -o jsonpath='{.spec.ports[0].port}' -n resource-sandbox




```





```


export FECB_CAPABILITY_API_SERVER_URL=172.3.0.1:30891

export token=\"UZKPYO0lescBh1DsVWJBhfV4sDoSF2rge0b1bdZ918Q=\"


./grpcurl  -cacert /opt/client/tls/ca-cert.pem -d "{\"token\":$token}" -import-path ./proto -proto capability-api.proto $FECB_CAPABILITY_API_SERVER_URL capability.CapabilityService/GetService


```


* format
    * hc
        * name/ip/port (svc)
    * dvc
        * name/ip/port (svc)
* get svc flow
    * get_service_json
        * permission(capability)
            * hc/dvc去找 (ServiceName/profilename)svc ip port
* issue
    * 一定要先new device才能get service(capability)






## 1/18
* 查核點對照表
* 作業手冊
* video tiip
```
    rm -rf /data/*
    #./setup.sh cert
    #put cert for harbor
    sudo mkdir -p /data/certs
    sudo cp certs/harbor-registry.crt /data/certs
    sudo cp certs/harbor-registry.key /data/certs    
    
    cp harbor.yml harbor
    cd harbor 
    docker-compose down -v
    ./prepare  --with-notary  --with-trivy
    docker-compose up -d
    
開瀏覽器
```




```
502 Bad Gateway, Msg : error sending request for url (https://minio.fecb-file-server.demo-nvidia.internal/fecb-file-server/?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ZDJhMmUxYzYzYTg4ZjA4YWIzZjExNTAy%2F20230117%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20230117T131712Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&encoding-type=url&list-type=2&X-Amz-Signature=c18f1a9acd7986967c99c26c619324e5ff84bef1972b938e3ae1ba930c7b55bf): error trying to connect: error:1416F086:SSL routines:tls_process_server_certificate:certificate verify failed:../ssl/statem/statem_clnt.c:1914: (unable to get local issuer certificate)
```
```
502 Bad Gateway, Msg : error sending request for url (https://minio.fecb-file-server.demo-nvidia.internal/fecb-file-server/?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ZDJhMmUxYzYzYTg4ZjA4YWIzZjExNTAy%2F20230117%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20230117T131706Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&encoding-type=url&list-type=2&X-Amz-Signature=dbf2ccccb8b6c91020dcab0522dd02499c9e0ac5dbaaacb643bc1927cecc8ba1): error trying to connect: tcp connect error: Connection timed out (os error 110)
```
## 12/12
* device cert
    * pem apply
    * query
    * 廢除
* notary
    * 架設harbor
    * 了解規格 畫圖
* gitlab
### code sign
* getver接通
* getCertificate
* codeSign

### device cert
### Notekm i
* block diagram ~ 1300
    * UML
        * use case diagram
        * activity diagram
        * sequence diagram
        * file server(是否需要)
* service ~1400
* harbor ~1500







房內附有冷/暖空調設備、睡墊、獨立衛浴、冰箱，車外部分附有遮雨棚、桌椅和照明燈光，請露友自備棉被、枕頭；
每房可住4人，超過4人，每人加收200元/晚，上限人數為5人；每間同行車數為1車，若超過1車，每車加收200/晚
夜衝請私訊營主

自備棉被枕頭
## 9/12
* dns certificate renew
* test pods 
https://www.youtube.com/watch?v=nL0x0LIpLlk
https://pfschina.org/wp/?p=1158
https://www.lategege.com/?p=818
https://ithelp.ithome.com.tw/articles/10266173
* godaddy
https://developer.godaddy.com/
## 9/11
https://n.yam.com/Article/20220908128603

* dns certificate renew
* test pods 



## 9/5
fiduciaedge/fecb-java-sdk:v1.4.1-x86
./grpcurl  -cacert /opt/client/tls/ca-cert.pem -import-path ./proto -proto capability-api.proto 172.3.0.1:30891 capability.CapabilityService/GetToken
./grpcurl  -cacert /opt/client/tls/ca-cert.pem -import-path ./proto -proto capability-api.proto fecb-capability-api.fecb-system.svc.cluster.local:65256 capability.CapabilityService/GetToken

* 50.66 capability api
* 6450 kernel
