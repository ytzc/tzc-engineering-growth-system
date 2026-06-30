# Container Sandbox Fecp

## 11/22
* 軍民meeting
    * 狄瑞
        * VPN tunnel(device ID cert from TWCA)
            * AK deviceID cert
            * 或是應用和軟體生產商cert
                * 另外做一個單純CSR apply cert
        * codesign做e2e file tranfer(option)
            * ccsars整合fecb-file
    * 軍民A3
        * CCSaaS
            * codesign blob
            * 燒錄韌體 整合service
            * 韌體demo
    * 劇本
        * camera
            * device container
            * 
        * hc
            * gpu container
            * wifi driver 簽名
        * app
            * app container
* 金要登錄平台
    * ek cert chain
    * private.pfx ap憑證申請
        * 以


* gary sumarize
* 11/21狄瑞 邊信連RD meeting
    * fECP v1.5(k8s aws)
    * Run update script from sandbox on vHub 筆電更新
    * Deploy update using network IP
    * VPN tunnel(device ID cert from TWCA)
    * codesign做e2e file tranfer(option)
# 11/21
* srs spec
* harbor架構 ota
* trusted thing架構
    * sequence diagram
    * use case

```
# Note
Trusted Things 可信物聯網設備解決方案 – 信任鏈概念
簡要描述軟體系統，包括目的、範圍、定義、引用文檔和總體描述。

* mtls通訊
    * 資料交換驗證雙方身分
    * 建立加密通道確保資料傳輸機密
* 容器化應用程式 (cosnar) 
    * 驗證容器來源及完整性
* 設備上運行容器化應用程式的sandbox  TEE-REE 執行環境(CCSars) 韌體codesign
    *  TEE-REE 執行環境
    *  隔離應用與設備，運算資料無法經硬體存取 
    *  隱私計算
* 啟動時驗證預載程式簽章(韌體 驅動 CCSars)
    * UEFI
    * TPM AK證明身分憑證
* 信任供應商 信任設備清單
* TPM產生信任跟


* A1註冊AK 金鑰登陸平台
    * 在每一個設備發起applycert, activatecredential
* A2申請AK憑證 物聯網
* A3系統軟體認證服務
    * CCSars
    * 軟體供應商對軟體簽章，簽名完提供給設備供應商
    * 設備供應商拿到簽名軟體，透過信任跟驗證簽名燒錄
    * 安全開機
* B1應用軟體認證服務
    * Cosnar
* B2安全容器沙箱
    * fECP
    * harbor OTA, notary signer
```
## 11/7
* fECP v1.5 spec summary
* 畫一張圖給owen 
    * container OTA update(用harbor)
* tss-esapi走完activate credential



# 10/24

```
while true; do grpc_health_probe -tls -tls-client-cert /tls/client/tls.crt -tls-client-key /tls/client/tls.key -tls-ca-cert /tls/server/ca.crt -addr 172.3.0.1:30891; sleep 1; done
```
```
while true; do ./grpc_health_probe -tls -tls-client-cert /opt/fiducia/tls/client-node.crt -tls-client-key /opt/fiducia/tls/client-node.key -tls-ca-cert /opt/fiducia/tls/server-ca.crt -addr 172.3.0.1:30891 -connect-timeout 1s; sleep 1; done

 ./grpcurl --key /opt/fiducia/tls/client-node.key --cert /opt/fiducia/tls/client-node.crt -cacert /opt/fiducia/tls/server-ca.crt -d "{\"service_name\":\"\",\"permission\":\"\",\"namespaces\":\"resource-sandbox\"}" -import-path ./proto -proto capability-api.proto 172.3.0.1:30891 capability.CapabilityService/CreateCapability
```


```
while true; do ./grpc_health_probe -tls -tls-client-cert /opt/fiducia/tls/client-node.crt -tls-client-key /opt/fiducia/tls/client-node.key -tls-ca-cert /opt/fiducia/tls/server-ca.crt -addr 172.3.0.1:30891 -connect-timeout 1s; sleep 1; done

 ./grpcurl --key /opt/fiducia/tls/client-node.key --cert /opt/fiducia/tls/client-node.crt -cacert /opt/fiducia/tls/server-ca.crt -d "{\"service_name\":\"\",\"permission\":\"\",\"namespaces\":\"resource-sandbox\"}" -import-path ./proto -proto capability-api.proto 172.3.0.1:30891 capability.CapabilityService/CreateCapability
```
* uninstall hook
    * remove IPPOOL
* init-container
* test-script
* file-api
* ota-api
sudo kubectl get pods -l app=device-pod -n resource-sandbox --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[0].metadata.name}'


libvirt lxc init path sbin init w

```
curl -o /usr/local/bin/kubectl -L "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x /usr/local/bin/kubectl
sudo kubectl get pods -l app=device-pod -n resource-sandbox --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[0].metadata.name}'

```




```
while true; do grpc_health_probe -tls -tls-client-cert /tls/client/tls.crt -tls-client-key /tls/client/tls.key -tls-ca-cert /tls/server/ca.crt -addr 172.3.0.1:30891; sleep 1; done

while true; do grpc_health_probe -tls -tls-client-cert /tls/client/tls.crt -tls-client-key /tls/client/tls.key -tls-ca-cert /tls/server/ca.crt -addr 172.3.0.1:30891 -connect-timeout 250ms; sleep 1; done


while true; do grpc_health_probe -tls -tls-client-cert /tls/client/tls.crt -tls-client-key /tls/client/tls.key -tls-ca-cert /tls/server/ca.crt -addr 172.3.0.1:30891 -connect-timeout 5s; sleep 1; done

while true; do grpc_health_probe -tls -tls-client-cert /tls/client/tls.crt -tls-client-key /tls/client/tls.key -tls-ca-cert /tls/server/ca.crt -addr :65256 -connect-timeout 1s; sleep 1; done
            Server::builder()
                .tls_config(identity.server_mtls().await)?
                .add_service(health_service)
                .add_service(CapabilityServiceServer::new(capability_service))
                .serve(addr)
                .await?;
                
                
                
  timeout: failed to connect service "172.3.0.1:30891" within 1s              

```
## 10/19
https://wiki.fiduciaedge.work/engineering/docs/docker-multiarch-image-build/setup/start?s[]=buildx
lvresize -l +100%FREE ubuntu-vg/ubuntu-lv --resizefs


  Warning  FailedScheduling  26s   default-scheduler  0/2 nodes are available: 2 node(s) had taint {node.kubernetes.io/disk-pressure: }, that the pod didn't tolerate.

  Warning  Failed     18s (x2 over 36s)  kubelet            Failed to pull image "fiduciaedge/calico-job:0.1": rpc error: code = Unknown desc = failed to pull and unpack image "docker.io/fiduciaedge/calico-job:0.1": failed to resolve reference "docker.io/fiduciaedge/calico-job:0.1": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
RUN apk --update add python3


pip3 install requests
```
Unable to connect to the server: tls: failed to verify certificate: x509: certificate signed by unknown authority

https://blog.csdn.net/a5534789/article/details/112848404


/etc/cni/net.d
  Warning  FailedScheduling  <invalid>  default-scheduler  0/2 nodes are available: 1 node(s) had taint {node.kubernetes.io/disk-pressure: }, that the pod didn't tolerate, 1 node(s) had taint {node.kubernetes.io/not-ready: }, that the pod didn't tolerate.
  
  
  
 bootstrap
 
   Normal   Scheduled  85s                default-scheduler  Successfully assigned fecb-system/fecb-cert-bootstrap-gkq2h to jerry-worker
  Normal   Pulled     78s                kubelet            Successfully pulled image "fiduciaedge/fecb-tls-bootstrap:v0.1.0" in 2.630814969s
  Normal   Pulled     76s                kubelet            Successfully pulled image "fiduciaedge/fecb-tls-bootstrap:v0.1.0" in 2.169203747s
  Normal   Pulled     60s                kubelet            Successfully pulled image "fiduciaedge/fecb-tls-bootstrap:v0.1.0" in 2.257289114s
  Normal   Pulling    30s (x4 over 81s)  kubelet            Pulling image "fiduciaedge/fecb-tls-bootstrap:v0.1.0"
  Normal   Created    28s (x4 over 78s)  kubelet            Created container fecb-tls-bootstrap
  Normal   Started    28s (x4 over 78s)  kubelet            Started container fecb-tls-bootstrap
  Normal   Pulled     28s                kubelet            Successfully pulled image "fiduciaedge/fecb-tls-bootstrap:v0.1.0" in 2.123075718s
  Warning  BackOff    4s (x7 over 75s)   kubelet            Back-off restarting failed container
```
# 10/13
* default-ns不能刪除 雞生蛋
```
sudo su
calicoctl apply -f calico-ip-pool.yaml 
calicoctl get ippools
calicoctl delete -f calico-ip-pool.yaml 


calicoctl apply -f agent-ns-ippool.yaml 
calicoctl delete -f agent-ns-ippool.yaml 

```

* agent-ns.ippool
* default-namespace.ippool
* fecb-system.ippool
* mgmt-ns.ippool
* resource-sandbox.ippool
## 9/19
* fECB API
    * Fix mtls environment variables to follow naming convention & set system-api mtls
* 自建cluster
    * watch
* proto 放api pod
* ota api
* 修改file-api
* grafana/loki
    * 動態hostname
* k8s
    * https://wiki.fiduciaedge.work/engineering/products/fecp/fecp_installation/start
    * eddie
        * https://hackmd.io/L1iAITrpRpSJUKuSBxvpjQ

* 度假攜帶
    * 手機 耳機 手錶 手電筒 露營燈 喇叭 耳罩
    * QuietComfort Ultra
## 9/4
* helm 書
* harbor helm佈署
* data helm

### select2pod2ip2db

* selector
* deploy_name
* 找到最新pod
* 找到ip


* selector -> pod/status/time -> latest pod name
```
sudo kubectl get pod -l app=device-selector -n resource-sandbox --no-headers -o jsonpath='{.items}'

sudo kubectl get pod -l app=device-selector -n resource-sandbox --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[0].metadata.name}'

sudo kubectl get pod -l app=device-selector -n resource-sandbox -o jsonpath='{.items[0].metadata.creationTimestamp}'
```




```
sudo kubectl get deployment -l app=device-selector -n resource-sandbox -o jsonpath='{.items[0].metadata.name}'


sudo kubectl get pod -l app=device-selector -n resource-sandbox --no-headers

sudo kubectl get pod -l app=device-selector -n resource-sandbox -o jsonpath='{.items[0].metadata.creationTimestamp}'

sudo kubectl get pod -l app=device-selector -n resource-sandbox -o jsonpath='{.items[0].metadata.name}'
```
## 8/28
* database pod

https://github.com/docker-library/docs/blob/master/mariadb/README.md
* cleanup
* init-container
* fecb bug
    * create capability不見
    * init container

## 8/21
mender 只會被mender.conf影響
* api
    * config mender client
    * config mender from conf
* ota-api
    * config client json
        * cp file done
    * health
        * 等待實作system api 搭配
    * status 
        * 先不做 坐在health
    * config inventory 
    * container pod
        * https://stackoverflow.com/questions/32163955/how-to-run-shell-script-on-host-from-docker-container
* todo
    * system get ver
    * ota health check
    * 
## 7/27
* Amazon Simple Storage Service (Amazon S3)
*  Key Encryption Service (KES) 
*  Key Management Service (KMS)

* pitis-cloud minio畫圖(2000-install)
    * kms
    * kes
    * minio
    * vault

* 修改/etc/hosts通過
    * 確認kubernetes的host resolve
### meeting
* 實作harbor對接scanner
* 討論registry要架設到那些政府雲是可用的(TWCC)

### issue
* docker login https://harbor.tiip.internal:30003
    * 才會有綠勾勾
    * push harbor.tiip.internal:30003
* docker login https://harbor.twca.com.tw
    * host resolve才會成功
## 7/3
* 測試報告
    * https://harbor.twca.com.tw/
    * https://notary.twca.com.tw/
* 使用手冊
* 錄影CosNAR
# 6/21
* harbor, vm, rust
## 6/20
* docker doc
* notary 成功
## 6/14
* 自架pistis cloud-harbor-server
* 自架notary signer
* client呼叫




parse error: Invalid numeric literal at line 1, column 6
* dekra
    * 先確定gary runall
    * 跑jerry debug8 密集測試 capability
    * 確認check function
* 先後順序
    * 先確定pod stable
    * 包裝roll up
    * annotation
    * 解checking function(plus)
    * sqlite3 改成postgres

* meeting
    * rollout 確保unit (podip)
    * annotation (clean up podip)
rollout
timestamp
* svc account

```
curl -H "Authorization: Bearer $K3S_TOKEN" https://kubernetes.default.svc.cluster.local/api/v1/namespaces/fecb-system/secrets/root-ca -k 

curl -H "Authorization: Bearer $K3S_TOKEN" https://kubernetes.default.svc.cluster.local/api/v1/namespaces/resource-sandbox/pods -k



```
* create issue1 dvc (debug6)
    * E0611 20:55:30.517865    4575 memcache.go:121] couldn't get resource list for external.metrics.k8s.io/v1beta1: the server is currently unable to handle the request
```
in capability

sudo kubectl get pods device-python-f9f899cff-jd2kl -n resource-sandbox -o jsonpath='{.status.phase}'

![](https://hackmd.io/_uploads/H1MENnmDh.png)


sudo kubectl get pods device-python-f9f899cff-8ppfm -n resource-sandbox -o jsonpath='{.status.phase}'  > out 2>error


kubectl get apiservice
v1beta1.external.metrics.k8s.io        monitoring/prometheus-adapter   False (FailedDiscoveryCheck) 

取得其他pod ip

改用
curl http://localhost:8080/api/v1/namespaces/default/pods

export K3S_TOKEN=$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)

curl -H "Authorization: Bearer $K3S_TOKEN" https://kubernetes.default.svc.cluster.local/api/v1/namespaces/fecb-system/secrets/root-ca -k | jq -r '.data["portainer-rootca.crt"]' | base64 -d



```
https://aptakube.com/blog/troubleshooting-api-resource-list

* 測試capability pod (debug8)
* create issue1 app(debug3)
```
sudo kubectl get pod -l app=app-selector -n default -o jsonpath='{.items[0].metadata.name}'
sudo kubectl get pod -l app=app-selector -n default -o json
```
# 6/12
* 書
    * rust 程式設計
    * harbor


## 6/11

* 兩個pod用相同selector輩分狀態(terminating, init)

```
[{"apiVersion":"v1","kind":"Pod","metadata":{"annotations":{"cni.projectcalico.org/containerID":"8968f26013722d779ceeb3bd25cf41f376f5ad79bbb521a274cba801da88cfe1","cni.projectcalico.org/podIP":"172.5.19.174/32","cni.projectcalico.org/podIPs":"172.5.19.174/32"},"creationTimestamp":"2023-06-11T09:28:44Z","deletionGracePeriodSeconds":30,"deletionTimestamp":"2023-06-11T10:39:16Z","generateName":"app-python-55f76665f8-","labels":{"app":"app-selector","pod-template-hash":"55f76665f8"},"managedFields":[{"apiVersion":"v1","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:annotations":{".":{},"f:cni.projectcalico.org/containerID":{},"f:cni.projectcalico.org/podIP":{},"f:cni.projectcalico.org/podIPs":{}}}},"manager":"calico","operation":"Update","time":"2023-06-11T09:28:45Z"},{"apiVersion":"v1","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:generateName":{},"f:labels":{".":{},"f:app":{},"f:pod-template-hash":{}},"f:ownerReferences":{".":{},"k:{\"uid\":\"b3eb2a0f-ca93-46a6-ac09-5b3b951da68d\"}":{".":{},"f:apiVersion":{},"f:blockOwnerDeletion":{},"f:controller":{},"f:kind":{},"f:name":{},"f:uid":{}}}},"f:spec":{"f:containers":{"k:{\"name\":\"my-pod\"}":{".":{},"f:args":{},"f:command":{},"f:env":{".":{},"k:{\"name\":\"NETWORK_INTERFACE\"}":{".":{},"f:name":{},"f:value":{}}},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:ports":{".":{},"k:{\"containerPort\":30502,\"protocol\":\"TCP\"}":{".":{},"f:containerPort":{},"f:protocol":{}}},"f:resources":{},"f:terminationMessagePath":{},"f:terminationMessagePolicy":{},"f:volumeMounts":{".":{},"k:{\"mountPath\":\"/.cache\"}":{".":{},"f:mountPath":{},"f:name":{}}}}},"f:dnsPolicy":{},"f:enableServiceLinks":{},"f:initContainers":{".":{},"k:{\"name\":\"clear\"}":{".":{},"f:args":{},"f:command":{},"f:env":{".":{},"k:{\"name\":\"SERVICE_SELECTOR_NAME\"}":{".":{},"f:name":{},"f:value":{}}},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:resources":{},"f:terminationMessagePath":{},"f:terminationMessagePolicy":{},"f:volumeMounts":{".":{},"k:{\"mountPath\":\"/.cache\"}":{".":{},"f:mountPath":{},"f:name":{}}}},"k:{\"name\":\"init-myservice\"}":{".":{},"f:args":{},"f:command":{},"f:env":{".":{},"k:{\"name\":\"DECRYPTED_FOLDER_PATH\"}":{".":{},"f:name":{},"f:value":{}},"k:{\"name\":\"FECB_CAPABILITY_API_SERVER_URL\"}":{".":{},"f:name":{},"f:value":{}},"k:{\"name\":\"FECB_FILE_API_SERVER_URL\"}":{".":{},"f:name":{},"f:value":{}}},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:resources":{},"f:terminationMessagePath":{},"f:terminationMessagePolicy":{},"f:volumeMounts":{".":{},"k:{\"mountPath\":\"/.cache\"}":{".":{},"f:mountPath":{},"f:name":{}}}}},"f:restartPolicy":{},"f:runtimeClassName":{},"f:schedulerName":{},"f:securityContext":{},"f:serviceAccount":{},"f:serviceAccountName":{},"f:terminationGracePeriodSeconds":{},"f:volumes":{".":{},"k:{\"name\":\"cache-volume\"}":{".":{},"f:emptyDir":{},"f:name":{}}}},"f:status":{"f:conditions":{"k:{\"type\":\"ContainersReady\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:message":{},"f:reason":{},"f:status":{},"f:type":{}},"k:{\"type\":\"Initialized\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:message":{},"f:reason":{},"f:status":{},"f:type":{}},"k:{\"type\":\"Ready\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:message":{},"f:reason":{},"f:status":{},"f:type":{}}},"f:containerStatuses":{},"f:hostIP":{},"f:initContainerStatuses":{},"f:podIP":{},"f:podIPs":{".":{},"k:{\"ip\":\"172.5.19.174\"}":{".":{},"f:ip":{}}},"f:startTime":{}}},"manager":"k3s","operation":"Update","time":"2023-06-11T09:28:48Z"}],"name":"app-python-55f76665f8-xxzfc","namespace":"default","ownerReferences":[{"apiVersion":"apps/v1","blockOwnerDeletion":true,"controller":true,"kind":"ReplicaSet","name":"app-python-55f76665f8","uid":"b3eb2a0f-ca93-46a6-ac09-5b3b951da68d"}],"resourceVersion":"20309950","uid":"21914a1e-73c2-4396-ae55-d635f56cd0ab"},"spec":{"containers":[{"args":["-c","while true; do echo hello; sleep 10;done"],"command":["/bin/sh"],"env":[{"name":"NETWORK_INTERFACE","value":"172.3.0.1:"}],"image":"fiduciaedge/fecb-sdk-python-example-app-sandbox:v1.4.1-x86_64","imagePullPolicy":"Always","name":"my-pod","ports":[{"containerPort":30502,"protocol":"TCP"}],"resources":{},"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File","volumeMounts":[{"mountPath":"/.cache","name":"cache-volume"},{"mountPath":"/var/run/secrets/kubernetes.io/serviceaccount","name":"kube-api-access-8t4vw","readOnly":true}]}],"dnsPolicy":"ClusterFirst","enableServiceLinks":true,"initContainers":[{"args":["ls"],"command":["/bin/bash","-c"],"env":[{"name":"SERVICE_SELECTOR_NAME","value":"app-selector"}],"image":"fiduciaedge/fecb-sdk-clear-sandbox:v1.4.3-x86_64","imagePullPolicy":"Always","name":"clear","resources":{},"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File","volumeMounts":[{"mountPath":"/.cache","name":"cache-volume"},{"mountPath":"/var/run/secrets/kubernetes.io/serviceaccount","name":"kube-api-access-8t4vw","readOnly":true}]},{"args":["./init.sh \u003e /.cache/log"],"command":["/bin/bash","-c"],"env":[{"name":"FECB_CAPABILITY_API_SERVER_URL","value":"172.3.0.1:30891"},{"name":"DECRYPTED_FOLDER_PATH","value":"/.cache/files"},{"name":"FECB_FILE_API_SERVER_URL","value":"http://172.3.0.1:30893"}],"image":"fiduciaedge/fecb-sdk-init-sandbox:v1.4.3-x86_64","imagePullPolicy":"Always","name":"init-myservice","resources":{},"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File","volumeMounts":[{"mountPath":"/.cache","name":"cache-volume"},{"mountPath":"/var/run/secrets/kubernetes.io/serviceaccount","name":"kube-api-access-8t4vw","readOnly":true}]}],"nodeName":"staging-worker","nodeSelector":{"katacontainers.io/kata-runtime":"true"},"overhead":{"cpu":"250m","memory":"160Mi"},"preemptionPolicy":"PreemptLowerPriority","priority":0,"restartPolicy":"Always","runtimeClassName":"kata-qemu","schedulerName":"default-scheduler","securityContext":{},"serviceAccount":"fecb-init-container-app","serviceAccountName":"fecb-init-container-app","terminationGracePeriodSeconds":30,"tolerations":[{"effect":"NoExecute","key":"node.kubernetes.io/not-ready","operator":"Exists","tolerationSeconds":5},{"effect":"NoExecute","key":"node.kubernetes.io/unreachable","operator":"Exists","tolerationSeconds":5}],"volumes":[{"emptyDir":{},"name":"cache-volume"},{"name":"kube-api-access-8t4vw","projected":{"defaultMode":420,"sources":[{"serviceAccountToken":{"expirationSeconds":3607,"path":"token"}},{"configMap":{"items":[{"key":"ca.crt","path":"ca.crt"}],"name":"kube-root-ca.crt"}},{"downwardAPI":{"items":[{"fieldRef":{"apiVersion":"v1","fieldPath":"metadata.namespace"},"path":"namespace"}]}}]}}]},"status":{"conditions":[{"lastProbeTime":null,"lastTransitionTime":"2023-06-11T09:28:44Z","message":"containers with incomplete status: [init-myservice]","reason":"ContainersNotInitialized","status":"False","type":"Initialized"},{"lastProbeTime":null,"lastTransitionTime":"2023-06-11T09:28:44Z","message":"containers with unready status: [my-pod]","reason":"ContainersNotReady","status":"False","type":"Ready"},{"lastProbeTime":null,"lastTransitionTime":"2023-06-11T09:28:44Z","message":"containers with unready status: [my-pod]","reason":"ContainersNotReady","status":"False","type":"ContainersReady"},{"lastProbeTime":null,"lastTransitionTime":"2023-06-11T09:28:44Z","status":"True","type":"PodScheduled"}],"containerStatuses":[{"image":"fiduciaedge/fecb-sdk-python-example-app-sandbox:v1.4.1-x86_64","imageID":"","lastState":{},"name":"my-pod","ready":false,"restartCount":0,"started":false,"state":{"waiting":{"reason":"PodInitializing"}}}],"hostIP":"192.168.50.66","initContainerStatuses":[{"containerID":"containerd://8a62d5a33400f32fccfa4836f7a6abcda0832452fb339661041f3187a649cb30","image":"docker.io/fiduciaedge/fecb-sdk-clear-sandbox:v1.4.3-x86_64","imageID":"docker.io/fiduciaedge/fecb-sdk-clear-sandbox@sha256:93d7e663ee23841a25d67f4263910e677549ea155e350a14ef977b87083a20e9","lastState":{},"name":"clear","ready":true,"restartCount":0,"state":{"terminated":{"containerID":"containerd://8a62d5a33400f32fccfa4836f7a6abcda0832452fb339661041f3187a649cb30","exitCode":0,"finishedAt":"2023-06-11T09:28:48Z","reason":"Completed","startedAt":"2023-06-11T09:28:48Z"}}},{"containerID":"containerd://f78fbd60f5ce8c640d83863c38857835680a58bcb6222fa07ccd4b7208f9da4b","image":"docker.io/fiduciaedge/fecb-sdk-init-sandbox:v1.4.3-x86_64","imageID":"docker.io/fiduciaedge/fecb-sdk-init-sandbox@sha256:645cf7a519a302b82825423946775a8ef90d7c29126bef1a58e04bd0c3b7000c","lastState":{"terminated":{"containerID":"containerd://f78fbd60f5ce8c640d83863c38857835680a58bcb6222fa07ccd4b7208f9da4b","exitCode":1,"finishedAt":"2023-06-11T10:33:44Z","reason":"Error","startedAt":"2023-06-11T10:33:38Z"}},"name":"init-myservice","ready":false,"restartCount":17,"state":{"waiting":{"message":"back-off 5m0s restarting failed container=init-myservice pod=app-python-55f76665f8-xxzfc_default(21914a1e-73c2-4396-ae55-d635f56cd0ab)","reason":"CrashLoopBackOff"}}}],"phase":"Pending","podIP":"172.5.19.174","podIPs":[{"ip":"172.5.19.174"}],"qosClass":"BestEffort","startTime":"2023-06-11T09:28:44Z"}},{"apiVersion":"v1","kind":"Pod","metadata":{"annotations":{"cni.projectcalico.org/containerID":"cf89f283739f9383c9a09282f9ac33b039a9dc7cf7eb1b6209f275175ca5489d","cni.projectcalico.org/podIP":"172.5.19.186/32","cni.projectcalico.org/podIPs":"172.5.19.186/32"},"creationTimestamp":"2023-06-12T00:13:42Z","generateName":"app-python-78674bc8d9-","labels":{"app":"app-selector","pod-template-hash":"78674bc8d9"},"managedFields":[{"apiVersion":"v1","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:annotations":{".":{},"f:cni.projectcalico.org/containerID":{},"f:cni.projectcalico.org/podIP":{},"f:cni.projectcalico.org/podIPs":{}}}},"manager":"calico","operation":"Update","time":"2023-06-12T00:13:43Z"},{"apiVersion":"v1","fieldsType":"FieldsV1","fieldsV1":{"f:metadata":{"f:generateName":{},"f:labels":{".":{},"f:app":{},"f:pod-template-hash":{}},"f:ownerReferences":{".":{},"k:{\"uid\":\"e8485c53-af96-4445-8edc-ffbf03614dc1\"}":{".":{},"f:apiVersion":{},"f:blockOwnerDeletion":{},"f:controller":{},"f:kind":{},"f:name":{},"f:uid":{}}}},"f:spec":{"f:containers":{"k:{\"name\":\"my-pod\"}":{".":{},"f:args":{},"f:command":{},"f:env":{".":{},"k:{\"name\":\"NETWORK_INTERFACE\"}":{".":{},"f:name":{},"f:value":{}}},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:ports":{".":{},"k:{\"containerPort\":30502,\"protocol\":\"TCP\"}":{".":{},"f:containerPort":{},"f:protocol":{}}},"f:resources":{},"f:terminationMessagePath":{},"f:terminationMessagePolicy":{},"f:volumeMounts":{".":{},"k:{\"mountPath\":\"/.cache\"}":{".":{},"f:mountPath":{},"f:name":{}}}}},"f:dnsPolicy":{},"f:enableServiceLinks":{},"f:initContainers":{".":{},"k:{\"name\":\"init-myservice\"}":{".":{},"f:args":{},"f:command":{},"f:env":{".":{},"k:{\"name\":\"DECRYPTED_FOLDER_PATH\"}":{".":{},"f:name":{},"f:value":{}},"k:{\"name\":\"FECB_CAPABILITY_API_SERVER_URL\"}":{".":{},"f:name":{},"f:value":{}},"k:{\"name\":\"FECB_FILE_API_SERVER_URL\"}":{".":{},"f:name":{},"f:value":{}}},"f:image":{},"f:imagePullPolicy":{},"f:name":{},"f:resources":{},"f:terminationMessagePath":{},"f:terminationMessagePolicy":{},"f:volumeMounts":{".":{},"k:{\"mountPath\":\"/.cache\"}":{".":{},"f:mountPath":{},"f:name":{}}}}},"f:restartPolicy":{},"f:runtimeClassName":{},"f:schedulerName":{},"f:securityContext":{},"f:serviceAccount":{},"f:serviceAccountName":{},"f:terminationGracePeriodSeconds":{},"f:volumes":{".":{},"k:{\"name\":\"cache-volume\"}":{".":{},"f:emptyDir":{},"f:name":{}}}},"f:status":{"f:conditions":{"k:{\"type\":\"ContainersReady\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:message":{},"f:reason":{},"f:status":{},"f:type":{}},"k:{\"type\":\"Initialized\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:message":{},"f:reason":{},"f:status":{},"f:type":{}},"k:{\"type\":\"Ready\"}":{".":{},"f:lastProbeTime":{},"f:lastTransitionTime":{},"f:message":{},"f:reason":{},"f:status":{},"f:type":{}}},"f:containerStatuses":{},"f:hostIP":{},"f:initContainerStatuses":{},"f:podIP":{},"f:podIPs":{".":{},"k:{\"ip\":\"172.5.19.186\"}":{".":{},"f:ip":{}}},"f:startTime":{}}},"manager":"k3s","operation":"Update","time":"2023-06-12T00:13:45Z"}],"name":"app-python-78674bc8d9-kc9fh","namespace":"default","ownerReferences":[{"apiVersion":"apps/v1","blockOwnerDeletion":true,"controller":true,"kind":"ReplicaSet","name":"app-python-78674bc8d9","uid":"e8485c53-af96-4445-8edc-ffbf03614dc1"}],"resourceVersion":"20524951","uid":"45034ce9-13fe-4af9-ad19-295971fb1e97"},"spec":{"containers":[{"args":["-c","while true; do echo hello; sleep 10;done"],"command":["/bin/sh"],"env":[{"name":"NETWORK_INTERFACE","value":"172.3.0.1:"}],"image":"fiduciaedge/fecb-sdk-python-example-app-sandbox:v1.4.1-x86_64","imagePullPolicy":"Always","name":"my-pod","ports":[{"containerPort":30502,"protocol":"TCP"}],"resources":{},"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File","volumeMounts":[{"mountPath":"/.cache","name":"cache-volume"},{"mountPath":"/var/run/secrets/kubernetes.io/serviceaccount","name":"kube-api-access-wz64g","readOnly":true}]}],"dnsPolicy":"ClusterFirst","enableServiceLinks":true,"initContainers":[{"args":["./init.sh \u003e /.cache/log"],"command":["/bin/bash","-c"],"env":[{"name":"FECB_CAPABILITY_API_SERVER_URL","value":"172.3.0.1:30891"},{"name":"DECRYPTED_FOLDER_PATH","value":"/.cache/files"},{"name":"FECB_FILE_API_SERVER_URL","value":"http://172.3.0.1:30893"}],"image":"fiduciaedge/fecb-sdk-init-sandbox:v1.4.3-x86_64","imagePullPolicy":"Always","name":"init-myservice","resources":{},"terminationMessagePath":"/dev/termination-log","terminationMessagePolicy":"File","volumeMounts":[{"mountPath":"/.cache","name":"cache-volume"},{"mountPath":"/var/run/secrets/kubernetes.io/serviceaccount","name":"kube-api-access-wz64g","readOnly":true}]}],"nodeName":"staging-worker","nodeSelector":{"katacontainers.io/kata-runtime":"true"},"overhead":{"cpu":"250m","memory":"160Mi"},"preemptionPolicy":"PreemptLowerPriority","priority":0,"restartPolicy":"Always","runtimeClassName":"kata-qemu","schedulerName":"default-scheduler","securityContext":{},"serviceAccount":"fecb-init-container-app","serviceAccountName":"fecb-init-container-app","terminationGracePeriodSeconds":30,"tolerations":[{"effect":"NoExecute","key":"node.kubernetes.io/not-ready","operator":"Exists","tolerationSeconds":5},{"effect":"NoExecute","key":"node.kubernetes.io/unreachable","operator":"Exists","tolerationSeconds":5}],"volumes":[{"emptyDir":{},"name":"cache-volume"},{"name":"kube-api-access-wz64g","projected":{"defaultMode":420,"sources":[{"serviceAccountToken":{"expirationSeconds":3607,"path":"token"}},{"configMap":{"items":[{"key":"ca.crt","path":"ca.crt"}],"name":"kube-root-ca.crt"}},{"downwardAPI":{"items":[{"fieldRef":{"apiVersion":"v1","fieldPath":"metadata.namespace"},"path":"namespace"}]}}]}}]},"status":{"conditions":[{"lastProbeTime":null,"lastTransitionTime":"2023-06-12T00:13:42Z","message":"containers with incomplete status: [init-myservice]","reason":"ContainersNotInitialized","status":"False","type":"Initialized"},{"lastProbeTime":null,"lastTransitionTime":"2023-06-12T00:13:42Z","message":"containers with unready status: [my-pod]","reason":"ContainersNotReady","status":"False","type":"Ready"},{"lastProbeTime":null,"lastTransitionTime":"2023-06-12T00:13:42Z","message":"containers with unready status: [my-pod]","reason":"ContainersNotReady","status":"False","type":"ContainersReady"},{"lastProbeTime":null,"lastTransitionTime":"2023-06-12T00:13:42Z","status":"True","type":"PodScheduled"}],"containerStatuses":[{"image":"fiduciaedge/fecb-sdk-python-example-app-sandbox:v1.4.1-x86_64","imageID":"","lastState":{},"name":"my-pod","ready":false,"restartCount":0,"started":false,"state":{"waiting":{"reason":"PodInitializing"}}}],"hostIP":"192.168.50.66","initContainerStatuses":[{"containerID":"containerd://de3078d297a5e2e00ef11302a411d145cb04c535b77f6b01e621afa23251193b","image":"docker.io/fiduciaedge/fecb-sdk-init-sandbox:v1.4.3-x86_64","imageID":"docker.io/fiduciaedge/fecb-sdk-init-sandbox@sha256:645cf7a519a302b82825423946775a8ef90d7c29126bef1a58e04bd0c3b7000c","lastState":{"terminated":{"containerID":"containerd://2ce022af5888ec72b8277aa11d1c1ecd48133ce2b220819776920986427dda70","exitCode":1,"finishedAt":"2023-06-12T00:15:36Z","reason":"Error","startedAt":"2023-06-12T00:15:05Z"}},"name":"init-myservice","ready":false,"restartCount":3,"state":{"running":{"startedAt":"2023-06-12T00:16:01Z"}}}],"phase":"Pending","podIP":"172.5.19.186","podIPs":[{"ip":"172.5.19.186"}],"qosClass":"BestEffort","startTime":"2023-06-12T00:13:42Z"}}]
```
* redploy
```
sudo cp fecb-supplements/fecb-system-api/fecb-system-api /opt/fiducia/bin

sudo systemctl daemon-reload
sudo systemctl start fecb-system-api.service
sudo systemctl enable fecb-system-api.service

```
* 發現
    * worker 跑去cloud(device)
    * rusqlite ->sqlx


```
DELETE FROM CAPABILITY WHERE ServiceName="app-selector";
```
### flow
* apply
    * gettoken(wait capability)
    * getservice(wait svc running/db)
    * getfile(wait prefetch)
* todo
    * init
        * Dockerfile-x86_64
        * init.sh
    * demo
        * demo.sh
    * capability
        * select改成svc
        * permission 改成用svc name(getservice) todo
            * createservice
                * check_podip_exist_and_write_to_database只放db查詢不用改
                * get_pods_name要改
## 5/24
https://juejin.cn/post/7073390068483751972
* 攻防情境
https://github.com/zj1244/Blog/blob/master/2019/harbor%E7%9A%84Notary%E5%8A%9F%E8%83%BD%E6%B5%8B%E8%AF%95.md
* ingress了解
```
{{- define "harbor.ingress" -}}
  {{- printf "%s-ingress" (include "harbor.fullname" .) -}}
{{- end -}}
``` 
* traefik了解
* drawio



## 5/23
* dns mapping path
    * 內部不要tls
```
get secret -o yaml
```

* notaery-servier.json
```
	"server": {
	  "http_addr": ":4443",
	  "tls_key_file": "/etc/ssl/notary-server/tls.key",
	  "tls_cert_file": "/etc/ssl/notary-server/tls.crt"	  
	},
```

* notary-server.yaml
```
        - name: notary-server
          mountPath: "/etc/ssl/notary-server"
          readOnly: true

      volumes:
      - name: notary-server
        secret:
          secretName: "harbor-ingress"
          
secret name 要去修 改對照
```

* get ca.crt
```
kubectl get secret -n container-registry harbor-ingress -o json | jq -r '.data["ca.crt"]' | base64 -d -
```
## 5/22
* 寫自己的helm chart(ok)
* secret selector(ok)
* notary server設定完成(ok)
* hc
* capability
* device
* fECB init.sh 1.4.3
* meeting
    * planet uml (design)
        * https://www.containerlabs.kubedaily.com/Kubernetes/beginner/Deployment-process.html
    * security
    
* docker manifest
* fECB helm
* todo
    *  Pod 的 Health Check
https://ithelp.ithome.com.tw/articles/10193956
## 5/15
* v1.4.3    
    * * demo
    * dvc
    * hc
    * capability
        * 重複create error code
        * 確認selector需要性
    * file

    * docker manifest
    * get ver
* harbor

## 5/8
* getsvc all
* pooling
* harbor

### pooling


* muti svc


```
kubectl get svc device-service-py -n resource-sandbox -o jsonpath='{.spec.clusterIP}'

kubectl get svc device-service-py -n resource-sandbox -o jsonpath='{.spec.ports[0].port}'

kubectl get svc device-service-py -n resource-sandbox -o jsonpath='{.spec.ports}'


kubectl get svc device-service-py -n resource-sandbox -o jsonpath='{.spec.ports}'

```
* K8S_API_SERVER_QUERY_RETRY_COUNTER
* K8S_API_SERVER_QUERY_TIMEOUT_DURATION_SEC
* svc->
* v1.4.2
    * capability: CapabilityName 移除
    * ProxyUUID

## 4/26
* muti svc
* harbor
## 4/25
* check_podip_exist_and_write_to_database




kubectl get pods -n resource-sandbox device-service-py-56f5487d54-78jrg -o jsonpath='{.status}'


kubectl get pods -n resource-sandbox device-service-py-56f5487d54-78jrg -o jsonpath='{.status.initContainerStatuses.state}'

* 正確status

```
{"conditions":[{"lastProbeTime":null,"lastTransitionTime":"2023-04-24T17:32:35Z","message":"containers with incomplete status: [init-myservice]","reason":"ContainersNotInitialized","status":"False","type":"Initialized"},{"lastProbeTime":null,"lastTransitionTime":"2023-04-24T17:32:35Z","message":"containers with unready status: [my-pod]","reason":"ContainersNotReady","status":"False","type":"Ready"},{"lastProbeTime":null,"lastTransitionTime":"2023-04-24T17:32:35Z","message":"containers with unready status: [my-pod]","reason":"ContainersNotReady","status":"False","type":"ContainersReady"},{"lastProbeTime":null,"lastTransitionTime":"2023-04-24T17:32:35Z","status":"True","type":"PodScheduled"}],"containerStatuses":[{"image":"fiduciaedge/fecb-sdk-python-example-device-sandbox:v1.4.1-x86_64","imageID":"","lastState":{},"name":"my-pod","ready":false,"restartCount":0,"started":false,"state":{"waiting":{"reason":"PodInitializing"}}}],"hostIP":"192.168.50.66","initContainerStatuses":[{"containerID":"containerd://ba2b80e538b16c3165fc6314f22964be342defd76728a988c1be1e78e7b47230","image":"docker.io/fiduciaedge/fecb-sdk-init-sandbox:v1.4.1-x86_64","imageID":"docker.io/fiduciaedge/fecb-sdk-init-sandbox@sha256:9ec5ff33a3e9ce6eabfda0e0c3e103140e6358f60d5e32a30ab99ea70a4e4742","lastState":{},"name":"init-myservice","ready":false,"restartCount":0,"state":{"terminated":{"exitCode":137,"finishedAt":null,"message":"The container could not be located when the pod was terminated","reason":"ContainerStatusUnknown","startedAt":null}}}],"phase":"Pending","podIP":"172.5.147.134","podIPs":[{"ip":"172.5.147.134"}],"qosClass":"BestEffort","startTime":"2023-04-24T17:32:35Z"}
```
* 錯誤status
```
{"conditions":[{"lastProbeTime":null,"lastTransitionTime":"2023-04-24T17:32:35Z","message":"containers with incomplete status: [init-myservice]","reason":"ContainersNotInitialized","status":"False","type":"Initialized"},{"lastProbeTime":null,"lastTransitionTime":"2023-04-24T17:32:35Z","message":"containers with unready status: [my-pod]","reason":"ContainersNotReady","status":"False","type":"Ready"},{"lastProbeTime":null,"lastTransitionTime":"2023-04-24T17:32:35Z","message":"containers with unready status: [my-pod]","reason":"ContainersNotReady","status":"False","type":"ContainersReady"},{"lastProbeTime":null,"lastTransitionTime":"2023-04-24T17:32:35Z","status":"True","type":"PodScheduled"}],"containerStatuses":[{"image":"fiduciaedge/fecb-sdk-python-example-device-sandbox:v1.4.1-x86_64","imageID":"","lastState":{},"name":"my-pod","ready":false,"restartCount":0,"started":false,"state":{"waiting":{"reason":"PodInitializing"}}}],"hostIP":"192.168.50.66","initContainerStatuses":[{"image":"fiduciaedge/fecb-sdk-init-sandbox:v1.4.1-x86_64","imageID":"","lastState":{},"name":"init-myservice","ready":false,"restartCount":0,"state":{"waiting":{"reason":"PodInitializing"}}}],"phase":"Pending","qosClass":"BestEffort","startTime":"2023-04-24T17:32:35Z"}
```

* 創建馬上拿pod ip
```
    kubectl apply -f $DVC_YAML -n resource-sandbox
| 


kubectl get pod -l app=device-service-py -n resource-sandbox -o jsonpath='{.items[0].metadata.name}' 


kubectl get pods  -n resource-sandbox -o jsonpath='{.status.podIP}'


```

* create capability fail
```
service/device-service-py created
deployment.apps/device-service-py created
ERROR:
  Code: Aborted
  Message:  [operation::create_user] create_user failed, DB: "transport error" 
13|usr-shaggy-grip|hc-service-py|hc-service-py-7b5c96994-h6555||resource-sandbox|HC_hc-service-py,Device_webcam-py|oFxHAVOBzAwjdx0fCrW4i_xnY2T3FubyhgQjBCZ7fDY=|2023-04-21 06:52:55



 INFO  fecb_capability_api::operation > enter create_capability
 INFO  fecb_capability_api::operation > permission: ""
 INFO  fecb_capability_api::utils     > ======== Try to get pod's name for service_name : device-service-py 
 INFO  fecb_capability_api::utils     > ======== Try to get pod's name for namespace : resource-sandbox 
 INFO  fecb_capability_api::operation > [operation::create_user::get_pods_name] get_pods_name success
 INFO  fecb_capability_api::utils     > [operation::utils::check_pod_exist_and_write_to_database] get pods
 INFO  fecb_capability_api::utils     > [operation::utils::check_pod_exist_and_write_to_database] pods status:"Pending"
 INFO  fecb_capability_api::utils     > [operation::utils::check_pod_exist_and_write_to_database] pods IP:""
 INFO  fecb_capability_api::utils     > [operation::utils::check_pod_exist_and_write_to_database] db params "usr-longing-property, device-service-py, device-service-py-56f5487d54-lghtm, , resource-sandbox, , GerTAFvpq4q8NFLiobe240xPlzt863O9yQo8K4_75lQ="
 ERROR fecb_capability_api::utils     > [operation::create_user] create_user failed, Msg= Write to DB error, transport error

```



```
watch -n 1 sudo kubectl get pods -n resource-sandbox device-service-py-7d8c8b9d9-kc8jr  -o jsonpath='{.status.phase}'



./grpcurl  -cacert /opt/client/tls/ca-cert.pem -d "{\"token\":\"K-az10T5r-wYsL-vCg2NVbROVvt9m7msQ7HIKjA6tP4=\"}" -import-path ./proto -proto capability-api.proto $FECB_CAPABILITY_API_SERVER_URL capability.CapabilityService/GetService | jq .svcAddress >> /.cache/svc.json


```

## 4/24


* capability api
	string service_name = 1;
	string permission = 2;
	string namespaces = 3;

* new device
* new hc

* sql server kubernete
SQL Server on Kubernetes: Designing and Building a Modern Data Platform






```
Ask for afternoon off on 4/28, one day leave on 5/2
Dear john,

I am writing this letter to apply 
my compensatory leave for taking afternoon off on 4/28(Friday 2 PM - 6 PM), 
my 初心假 for taking one day leave on 5/2
I will be back to work on the 5/3 (Thursday), 
kindly please approve.

Best Regards,
Jerry

```


lens ide

TFhHos45lR1912uSIEzxe_XzcWp5Mpj2d2B4wsCNZDA=
TFhHos45lR1912uSIEzxe_XzcWp5Mpj2d2B4wsCNZDA=
```
 INFO  fecb_file_api::reception > Get file request
 INFO  fecb_file_api::utils     > user_token : jerV8xvJGnqg7g3hhP5ksFpbxljdFq6aDebnqsa8Xgg=
 INFO  fecb_file_api::utils     > permission File_Y2EucGVt,HC_hc-service-py,Device_webcam-py
 INFO  fecb_file_api::reception > Get file Y2EucGVt
 INFO  fecb_file_api::reception > path : /media/hdd/data/sealed/Y2EucGVt
 INFO  fecb_file_api::utils     > machine_decrypt_data
 INFO  fecb_file_api::utils     > Machine key: "a964604696b13e86d0e296c786c8a2baa3f9612a9aa8c64634086bf4fedefe50"
 INFO  fecb_file_api::utils     > read rst 1048576
 INFO  fecb_file_api::utils     > read rst 1048576
```
```
export FECB_FILE_API_SERVER_URL="http://172.3.0.1:30893"

mkdir /opt/client/tls
docker cp /opt/client/tls/* fb4a5055959e:/opt/client/tls

mkdir /.cahce

 ./getfile PzNfjT_AkwLkHYYesp-L6LzyU3ABEYMxNqGddlrXm80= .


export DECRYPTED_FOLDER_PATH=/.cache/files
 
 
./getfile PzNfjT_AkwLkHYYesp-L6LzyU3ABEYMxNqGddlrXm80= /.cache/files
 
fiduciaedge/fecb-sdk-init-sandbox:v1.4.1-aarch64
```

```
kubectl get pods device-service-py-6d868fd774-z8qkm -o jsonpath='{.spec.containers[0].ports[0].containerPort}' -n resource-sandbox 

kubectl get pods device-service-py-65c687d97d-ln646 -o jsonpath='{.spec.containers[0].ports[0].containerPort}' -n resource-sandbox 



device-service-py-6d868fd774-z8qkm
```
* harbor helm chart HA筆記完成
* 1筆記完成(4/8)
* harbor HA部屬驗證
* 3,4筆記完成


## 4/14
* harbor
* notary

# 2/28
* ckpt meeting
    * ccsars cosnar有兩個模型需要準備(yolo)
    * 攻擊情境 攻擊驗證服務 準備攻擊
    * 查核點逐項備著說明
    * 終極警探4
        * 現場展示iot攻擊成功 demo編劇
    * 三階段
        * 1.腦力激盪(現場展示攻擊劇本)用餐
        * 2.收斂變成事項清單
        * 3.執行過程

## 2/13
* harbor登入
* 上傳映像檔成功
* trivy報告
* SBOM報告
* IO狀態
## 2/7
* device cert影片
* notary sign 影片
    * 架設harbor server
    * 架設notary server
* notary sign架構



* notary
    * 沒有notary sign的push(DOCKER_CONTENT_TRUST=0) 實作push差異
## 2/2
* ccsars影片 2分鐘
* cosnar影片 3分鐘



* ccsars
    * demo整理 ~2000
    * 6450測試 ~2030
    * 架構圖 ~2100
    * 錄影片 ~0000
## 1/30
* massfuse
* tiip demo


```
sudo mkdir -p /data/certs
sudo cp certs/harbor-registry.crt /data/certs
sudo cp certs/harbor-registry.key /data/certs    

./prepare  --with-trivy
sudo docker-compose up -d
docker-compose ps

開瀏覽器


docker login https://192.168.10.215:343 -u admin -p Harbor12345
export DOCKER_CONTENT_TRUST=0

docker pull fiduciaedge/fecb-agent:v1.4.1-x86-test
docker tag fiduciaedge/fecb-agent:v1.4.1-x86-test 192.168.10.215:343/test/fecb-agent:test
docker push 192.168.10.215:343/test/fecb-agent:test

瀏覽器 漏洞游標 export CVE



docker run --rm fiduciaedge/tern:v1 report -i fiduciaedge/fecb-agent:v1.4.1-x86-test

docker run -v /var/run/docker.sock:/var/run/docker.sock --rm fiduciaedge/dfimage:v1 a5a7f6285c2b > Dockerfile

trivy fs --security-checks config ./Dockerfile


docker run -p 9000:9000 --rm -v /var/run/docker.sock:/var/run/docker.sock fiduciaedge/container-webui:v1

```

### docker compose 理解

## 12/14
* pistis
* 錄製api sdk
## 12/13
* wifi dongle
* openvpn
* pistis
* 錄製api sdk
## 9/15
* harbor notary server溝通
* container cncf notary
* signer 簽名
# 9/5

KUBERNETES_MASTER
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
172.10.89.54


```
IP 172.10.89.54 is in use
Attributes:
  namespace: default
  node: staging-worker
  pod: example-java-f64c8dd98-kbrzg
  timestamp: 2022-09-05 07:43:43.555475347 +0000 UTC
  
  IP 172.7.69.69 is in use
Attributes:
  pod: fecb-capability-api-5fcdbcbbcf-9q77z
  timestamp: 2022-09-05 08:12:33.957289787 +0000 UTC
  namespace: fecb-system
  node: staging-worker
  
```
