# Twca Code Signing Sandbox

## 10/26
* 跑一次
    * gpgsm --list-key --with-validation
* gpgsm
```
gpgsm -K ansible test Root CA
gpgsm --import server-ca.crt 
gpgsm --disable-crl-checks --verify test.cms 
gpgsm --disable-crl-checks --verify test.cms <(echo "your_input_string_here")

gpgsm --list-keys 
查看ID

```
* note
    * gpgsm --disable-crl-checks --verify test.cms
        * pod 找不到rootca
    * gpgsm --list-keys
        * pod的CN ansible test Intermediate CA
        * 放在最底層
    * gpgsm -K ansible test Root CA
    * gpgsm -K ansible test Intermediate CA
    * installed and marked as trusted 
        * gpgsm --edit-key 0x0A408B46
    * cert ID
        *  0x25F74A48
    *  指紋
        *  E7:F8:BD:EA:E0:6B:3E:BE:4D:B5:0C:B6:39:56:D4:D7:0A:40:8B:46
        *  gpg-agent configure
        *  trustlist.txt
    *  /opt/fiducia/.gnupg
    *  APPDATA/GNU/etc/gnupg/trustlist.txt
    *  https://www.gnupg.org/documentation/manuals/gnupg/Agent-Options.html#option-_002d_002dhomedir
    *  ~/.gnupg/trustlist.txt
    *  manually adding the certificate's fingerprint to the trustlist.txt
        *  gpgsm --keyring trustlist.txt --disable-crl-checks --verify test.cms
        *  gpgsm: dirmngr cache-only key lookup failed: No dirmngr
    
* cert fidderenet
```
gpgsm --disable-crl-checks --verify test.cms

woking node
gpgsm: Signature made 2023-10-26 04:27:10 using certificate ID 0x25F74A48

failing node
gpgsm: Signature made 2023-10-26 04:27:10 UTC
gpgsm:                using rsa2048 key 6734353EA8C577141E6C67B90E2D8C1225F74A48

why different to the same test.cms
ChatGPT
The difference in the gpgsm output between the working node and the failing node when verifying the same test.cms file may be due to variations in how the nodes are configured, especially with regard to the certificates and trust settings. Let's break down the differences you've highlighted:

Working Node Output:

gpgsm: Signature made 2023-10-26 04:27:10 using certificate ID 0x25F74A48
Failing Node Output:

gpgsm: Signature made 2023-10-26 04:27:10 UTC
gpgsm: using rsa2048 key 6734353EA8C577141E6C67B90E2D8C1225F74A48
The working node's output indicates that it successfully verified the signature of test.cms using the certificate ID 0x25F74A48.

The failing node's output, on the other hand, indicates a couple of things:

It correctly verifies the signature made on test.cms with a timestamp of "2023-10-26 04:27:10 UTC."
It mentions the key ID (6734353EA8C577141E6C67B90E2D8C1225F74A48) used in the signature.
The key difference in the failing node's output is that it provides more detailed information about the key (6734353EA8C577141E6C67B90E2D8C1225F74A48) used in the signature verification, which is not present in the working node's output.

This additional information can be useful for troubleshooting and understanding the certificate chain and key used in the verification process. The fact that it provides information about the key used (6734353EA8C577141E6C67B90E2D8C1225F74A48) is not necessarily a sign of a problem but rather an additional level of detail in the output.

To address the issue of trust and the root certificate not being marked as trusted on the failing node, you should follow the steps mentioned in the previous responses to ensure that the root certificate is correctly installed and marked as trusted on the failing node. Once the root certificate is trusted, the failing node should be able to verify the signature of test.cms just like the working node.






```
* test

https://www.gnupg.org/documentation/manuals/gnupg/Howto-Create-a-Server-Cert.html
gpgsm -K ansible test Root CA
update-ca-certificates

gpgsm --disable-crl-checks --verify test.cms 

gpgsm --import

* tmp

r marking certificates as trusted or editing keys. 


To resolve the issue, you should follow the steps provided earlier to mark the root certificate as trusted on the failing node using the gpgsm --edit-key command:

bash
Copy code
gpgsm --edit-key 0x0A408B46
trust
5  # Select "I trust ultimately"
save
This should mark the root certificate as trusted on the failing node and allow it to be used for signature verification without encountering the "root certificate is not marked trusted" error.
```
    info!("utils::gpgsm_verify::echo_out {:?}",echo_out);
    let output = Command::new("gpgsm")
        .stdin(Stdio::from(echo_out))
        .arg("--disable-crl-checks")
        .arg("--verify")
        .output()
        .expect("Failed to start gpgsm process");
        
     gpgsm --disable-crl-checks --verify test.cms [string here]
        
```

```
gpgsm: Signature made 2023-10-26 04:27:10 UTC
gpgsm:                using rsa2048 key 6734353EA8C577141E6C67B90E2D8C1225F74A48
gpgsm: root certificate is not marked trusted
gpgsm: fingerprint=E7:F8:BD:EA:E0:6B:3E:BE:4D:B5:0C:B6:39:56:D4:D7:0A:40:8B:46
gpgsm: DBG: BEGIN Certificate 'issuer':
gpgsm: DBG:      serial: 6C7F598D979C1E17FEA4E556E974467BD44CF8F6
gpgsm: DBG:   notBefore: 2023-10-24 07:36:33
gpgsm: DBG:    notAfter: 2033-10-21 07:36:33
gpgsm: DBG:      issuer: CN=ansible test Root CA,OU=ansible test Root CA,O=FiduciaEdge,L=Hsinchu,ST=Hsinchu,C=TW
gpgsm: DBG:     subject: CN=ansible test Root CA,OU=ansible test Root CA,O=FiduciaEdge,L=Hsinchu,ST=Hsinchu,C=TW
gpgsm: DBG:   hash algo: 1.2.840.113549.1.1.11
gpgsm: DBG:   SHA1 Fingerprint: E7:F8:BD:EA:E0:6B:3E:BE:4D:B5:0C:B6:39:56:D4:D7:0A:40:8B:46
gpgsm: DBG: END Certificate
gpgsm: after checking the fingerprint, you may want to add it manually to the list of trusted certificates.
gpgsm: invalid certification chain: Not trusted
", metadata: MetadataMap { headers: {"content-type": "application/grpc", "date": "Thu, 26 Oct 2023 08:23:05 GMT", "content-length": "0"} 
```
## 8/10
* tiip~21:00
    * hacker 網頁
    * demo script function
        * 00-config
        * 010-push-unsigned-image
        * 011-deploy-unsigned-image
            * 成功 192.168.10.215:3447
        * 012-push-signed-image
            * harbor ui顯示綠勾
            * harbor掃描
        * 013-deploy-signed-image
            * 打開網頁說明
        * 014-remove-signature

        * 020-attack-poisoned-unsigned
            * webui更改成功
            * 011 失敗拒絕沒簽名
        * 021-attack-poisoned-signed
            * 推送失敗 沒有鑰匙
            * 刪除失敗 沒有鑰匙
            * 014刪除簽名
            * 推送signed失敗
            * 推送unsigned成功 deploy 失敗
    * 3-1影片
    * demo影片
        * 正規
        * 攻防
* mender 21~23
    * configure
    * getfile 
## 8/9
* tiip meeting
    * 3-1影片 五分鐘
        * 錄製旁白
    * demo一間房間 可以的話兩個螢幕
        * 一個螢幕駭客 右下角駭客人畫面
        * 一個螢幕後台展示作法
    * 沒有攻防不超過十分鐘
    * 攻防演練不超過五分鐘
        * 被hacker 改某一個畫面(改html 駭客logo顯示在index.html 小圖呈現)
    * script簡體字
        * 改成linux shell script
        * function處理
    * 強調harbor相關字眼說明signer設計
    * him醫療相關 強調相關性
    * 展示內容(畫面)
        * 兩台主機 
            * 駭客 Jerry筆電(外借)
            * 使用者/架構展示 Jerry主要筆電
            * TWCA 家宏筆電
        * 螢幕 主原則 兩台螢幕
            * 1. 架構ppt動畫 大投影
            * 2. 後台(駭客/使用者/TWCA 可走瀏覽器 待討論)
        * 螢幕 較佳備案 三台螢幕
            * 1. 架構ppt動畫 大投影
            * 2. 左後台(駭客)
            * 3. 右後台(使用者/TWCA 可走瀏覽器 待討論)
    * schedule
        * 8/17 四 10:00 排演demo 確認流程
            * twca2樓 兩個螢幕 下午討論歐文
            * gopro錄影
        * 8/18 五 上午完成備用demo影片
            * 開會錄音走一遍
            * demo螢幕上走一遍
            * 考前猜題
        * 8/23 三 最終查核TWCA
    * 內容討論
        * 上傳tuf 用command line(script function)

* tiip
    * hacker 網頁
    * 3-1影片
    * demo影片
        * 正規
        * 攻防
* mender
    * configure
    * getfile 
## 8/8
* mender server client
    * server install
        * Production installation with Kubernetes
    * client install
        * installing
        * Use an Update Module
        * Use the Device-side API
        * Configuration file
    * Artifact creation
        * Sign and verify
* mender API
    * https://docs.mender.io/api/#introduction
## 7/14
* 投影片動畫
    * 正常推image 駭客置換
    * 說明DCT
    * DCT push
    * 轉成CoSNAR
    * pull sign image
    * pull unsigned image
    * hacker pull remove
    * owner移除簽名
    * 駭客假裝簽名失敗
    * 駭客上傳無簽名覆蓋 部屬失敗
    * 
## 7/4
* test api(已改完)
    * TestCryptoSignerInterfaceBehaviorTWCA(Ok)
    * healthcheck(有時間測試, 可能週三)
* harbor ca(先不管cert issue)
    * harbor放客戶端由客戶設定
        * 先不管，給對外機使用，對外機在管理certificate
    * 未來放在合適的雲端位置(AWS)
* port(待測notary)
    * 30003, harbor registry使用(OK)
        * harbor.twca.com.tw
    * 30004, notary server對外使用(待測)
        * notary.twca.com.tw
## 6/25
* go call local module
    * https://stackoverflow.com/questions/52026284/accessing-local-packages-within-a-go-module-go-1-11
* go test api
* 比對twca
## 6/23
* go hello world
* gitgub notary signer模擬
* go grpc server
* go-signer
* signer io
* twca signer



* auto zsh

```
docker run -p 127.0.0.1:30892:39180 -v /opt/client/tls:/opt/client/tls --env SERVER_CERT_PATH=/opt/client/tls/server-cert.pem SERVER_KEY_PATH=/opt/client/tls/server-key.pem CA_CERT_PATH=/opt/client/tls/ca-cert.pem
```
## 6/15
* 自建harbor server切割signer 實作
## 5/31
* 修改
    * capability util
        * 109 select ServiceName from device (getservice)

* notary 自己架設
https://github.com/notaryproject/notary/blob/master/docs/running_a_service.md
* 確認server證書
* notary signer分離
* 攻防情境
## Todo

- Modify harbor templates for notary-server
    - Notary-sign test with CLI
    - Notary-sign test with gRPC

- Offensive and Defensive Exercise document (CoSNAR)~**5/31**

- fECB v1.4.3 ~**6/1**

- Set up traefik routing for TWCA


## 5/29
* tiip
    * tuf signature
    * 攻防情境
### dev
* notary sign
* grpc
* documnet
## 5/23
* modify
    * client: 192.168.10.217
* Test notary function via image signature
    * Create testing script
    * Verify image's signature
* CoSNAR notary function
* Draw sequence diagram
https://github.com/zj1244/Blog/blob/master/2019/harbor%E7%9A%84Notary%E5%8A%9F%E8%83%BD%E6%B5%8B%E8%AF%95.md


## 2/8
* meeting
    * 全配字幕 淺顯易懂 這一步目的是甚麼 
        * 改成投影片顯示 講到哪裡只到哪裡
            * 子畫面 螢幕錄製
            * 指令放附錄
            * 目標導向 結果導向
    * ccsars
        * 字幕說明整段過程
        * 補上twca cert
        * 強調紅色方框
    * cosnar
        * https://blogs.vmware.com/vmware-taiwan/2018/05/31/pks-%E6%BC%94%E7%A4%BA-%E5%AE%B9%E5%99%A8%E6%98%A0%E5%83%8F%E5%80%89%E5%BA%AB-harbor/
        * microsoft azure 文字轉語音 yunJhe 1.0 General
        * 5 6 分鐘結束
        * trivy指向notary
        * notary signer
        * 開頭的部分
* flow
    * ccsars (一小時)
        * 介紹secure boot
        * 介紹code sign
            * 實作hash
            * 驗證secure boot
        * 介紹device cert
            * 實作device cert
    * cosnar (一小時)
        * 介紹harbor
        * 介紹notary
            * 實作sign
            * 驗證unsigned
        * 介紹trivy
            * 實作scan
        * 介紹scanner
            * 報告展示
* 介紹 sb codesign ~2130
* 實作 device cert 2150

## 1/6
* overview
    * notary signer
        * Sign
        * CreateKey
        * delete
* 接通自己的notary server
    * 架設notary server
        * 去掉--with-notary
        * --with-notary
        * 建立notary
        * docker run server
            * 了解筆記
            * 建立signer
        * docker run signer
        * 遠端連線 
    * client, server, signer 設定
        * notary server -> twca signer
    * docker compose yml修改
    * 觀察log
* 分離自己的notary signer
* 連通台網的notary signert
* 轉成kubenete
## 12/23


###jar test
#java -jar codesign.jar getVer
#java -jar codesign.jar getCert fe_prod_soft
#sha=($(shasum -a 256 shimx64.efi))
#echo $sha > unsigned_hash
#java -jar codesign.jar Sign fe_prod_soft unsigned_hash signed_hash
#java -jar codesign.jar Attach certb64 shimx64.efi  signed_hash  p7_sig
#sbattach --attach p7_sig shimx64.efi
#sbverify --list grubx64.efi
#sbattach --remove grubx64.efi
###UEFI teset
## 12/19
* notary signer

## 12/18
* notary signer
* codesign grpc
* 
## 12/14
* gitlab
* 瑞峰
    * sign
    * csr

# deadline
* 12/3 12:00 keyhost/fusing host
* 12/3 22:00 flashing host/sign host
* 12/4 codesign notary

# 行程規劃
* 12/2 keyhost/ fusinghost
* 12/3 flashing host/sign host
* 12/4 codesign notary

## 12/1
* meeting
    * 軟體排程
    * TAA(PE) 流程手畫 手冊 (呈現無視 8221 intel)
    * 下週五要去跑 明天內部(這禮拜有點趕 下周一安裝 下周三ready)
    * 驗收單
* 進度
    * 8221 (1400)
    * notary signer(1600)
    * 架構圖 (連線台網過程, 過程)
    * 手冊
    * deploy
## 11/29
* codesign service (notary signer)
## 10/18
* rust pod ip
* ai inference
* notary
* codesign service rust
## 10/17
* rust service
    * 書1~5
    * code hash 
    * code sign
## 10/12
* 11月中 locus做到 codesign
    * image
* 12月底 做到OTA
## 10/5
* codesign service
    * sign
## 10/4
* harbor架設完畢
* codesign hash
* 畫圖
## 10/3
* harbor架設 (k3s master) helm
* notary / cosign
* codesign service 
    * hash code
    * code sign
## 9/29
* codehash
* codesign
* https://doc.rust-lang.org/book/ch18-03-pattern-syntax.html#destructuring-nested-structs-and-enums
## 9/26
* 6450 test腳本
* codesign rust
    * hashcode
    * signcode
    * buildp7
    * csr
## 9/22
* hashcode
    * 上傳stream
    * 做hash
    * 回hashed
* listversion
### todo
* hashcode
    * https://www.vinsguru.com/grpc-file-upload-client-streaming/
    * upload streaming
    * hashcode
* listversion

## 9/19
* https://cloud.tencent.com/developer/article/1832918



* meeting
    * harbor的verify外包出來實行，code不要讓我們看到
    * 讓開發者覺得不用洩漏code
    * https://goharbor.io/docs/2.5.0/working-with-projects/project-configuration/implementing-content-trust/
* vHub AI inference 十二月初demo
uml流程圖

```
Ask for taking the half day leave on 9/22 and 生日假 on 9/23

Dear John,

I am writing this letter to apply my annual leave for taking the afternoon off on 9/22(Thursday) and 生日假 on 9/23(Friday), I will be back to work on the 9/26 (Monday), 
kindly please approve.

Best Regards,
Jerry

```
## 9/10
* test pods
* twca client
## 8/29
* 影片
    * 左OEM
    * 右TWCA client
    * 右下資料傳遞區
## 8/27
* sign, hash, verify image
## 8/26
* demo情境slide
    * A3.1
        1. 開發能在可信執行環境 (TEE)中運算SHA-256雜湊值程式碼映像檔的「安全程式碼雜湊運算模組」
        2. 將程式碼雜湊模組封裝成兼容於OCI的容器映像檔
        3. 在 FiduciaEdge可信邊緣運算平台 (fECP) 上的安全沙箱中佈署和執行容器化的安全程式碼雜湊運算模組
    * A3.2
        1.	在用戶開發環境中的容器化程式碼簽章客戶端與在TWCA環境中的伺服器之間在HTTPS + mTLS + JSON Web Token (JWT) 保護下進行相互認證、不可否認和資料保密的交易功能
        2.	程式碼簽章客戶端和伺服器之間具有rollback功能的原子化交易功能
        3.	程式碼雜湊和簽章解耦之安全交易的應用程式
        4.	程式碼映像檔和密鑰分發之安全交易的應用程式
        5.	TWCA發行在交易中使用的X.509公鑰證書


* java code(verify) ~1430
    * p1 build失敗, 實作p7
* java container ~1500
* 影片 ~1530
* secure boot ~1600
* pistis ~1630
* OTA update 晚上
## 8/25
* p1, p7
    * 書4567
* sign hash verify code
![](https://i.imgur.com/hyhfcq3.png)
* docker image, sandbox
* secure boot
    * https://www.youtube.com/watch?v=Td4o7b24I28
* 重新佈署pistis 
## 8/24
* meeting
    * 需求建議書
        * server會上雲端
        * 不做ZERO TRUST怕node可以調整server調整
        * server可以調整
    * 開會
        * 明日8221 燒錄pbkey, signed system software, end to end securuty(設定改動)
        * 1.
            * 原本出場就燒好(組裝廠做的, 停車住組裝時做的)
            * 燒錄自己的應用軟體, linux再組裝廠燒得
            * 炎陽給的機器是空的, 炎陽工廠燒比較輕鬆
            * 一台20分鐘, 可以一次燒好幾台
* p1, p7
    * 書4567
* sign hash verify code
![](https://i.imgur.com/hyhfcq3.png)
* docker image, sandbox
* secure boot
    * https://www.youtube.com/watch?v=Td4o7b24I28

## Nano
```
package com.fiducia;


import java.io.*;
import java.math.BigInteger;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.Signature;
import java.security.PublicKey;
import java.util.Base64;

public class SignService {
    public static void main(String[] args) throws Exception {
        API.getVer();
        System.out.println("java -jar .\\codesign-v1.4.0.jar getVer");


        /*
        if(args.length == 0)
            return ;

        if (args[0].compareTo("getVer")==0)
            try{
                API.getVer();
            } catch (Exception e) {
                e.printStackTrace();
            }
        */





        //openssl dgst -sha256 -verify pk -signature signedhash codehash

        Cert cert = new Cert("fe_prod_soft");
        cert.pem2file("cert.pem");


        //byte[] byteFile =  utils.File2Byte("codehash");
        //byte[] bytehash = hexStr2Byte(new String(byteFile));

        String strFile= utils.File2Str("codehash");
        byte[] bytehash = hexToBytes(strFile);



        Key.listKey();
        Key.keyActive("fe_prod_soft");

        Sign sign = new Sign("fe_prod_soft");
        String signedhash= sign.SignHash(bytehash);
        System.out.println(signedhash);


        //utils.Str2File(signedhash,"signedhash.sha256");
        //Key.keyDeactive("fe_prod_soft");


        //boolean rst=Verify.testsign(signedhash,"fe_prod_soft",bytehash);



    }



    public static byte[] hexToByteData(String hex)
    {
        byte[] convertedByteArray = new byte[hex.length()/2];
        int count  = 0;

        for( int i = 0; i < hex.length() -1; i += 2 )
        {
            String output;
            output = hex.substring(i, (i + 2));
            int decimal = (int)(Integer.parseInt(output, 16));
            convertedByteArray[count] =  (byte)(decimal & 0xFF);
            count ++;
        }
        return convertedByteArray;
    }

    public static byte[] hexToBytes(String hex){
        hex = hex.length() % 2 != 0 ? "0" + hex : hex;

        byte[] b = new byte[hex.length() / 2];
        for(int i = 0 ; i < b.length; i ++){
            int index = i * 2;
            int v = Integer.parseInt(hex.substring(index,index+2), 16);
            b[i] = (byte) v;
        }
        return  b;

    }
}
```
## 8/23



* 雙蓋摺疊小包 1600 BEB03
* 拉鍊萬用小包 680
* 名片零錢兩用小包 680

* demo
    * get code(from minio)
    * do hash(hash sandbox)傳到sign sandbox
    * sign hash(sign sandbox)上傳minio
    * verify
* todo
    * java getfile
    * java hash,sign
    * sandbox
    * verify

* OEM
    * hash sandbox
        * hashtool.jar
        * code -> `java -jar hashtool -i code -o hashedcode` -> hashedcode
    * sign sandbox(service)
        * signtool.jar(daemon)
        * hashedcode ->`java -jar signtool -i hashedcode -o signed` -> signed
* User
    * verify sandbox
        * signed, code, cert -> `java -jar verifytool -i--sign signed -i--code code -i--cert cert -o result ` -> result
### hash, sign, verify
## 8/22

https://developer.nvidia.com/embedded/jetson-linux-archive
https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3261/index.html#page/Tegra%20Linux%20Driver%20Package%20Development%20Guide/adaptation_and_bringup_nano.html
![](https://i.imgur.com/hyhfcq3.png)

* code
    * hash (~1420)
    * sign (~1440)
    * attach (~1500)
    * verify
    * service 傳遞
```

    public Resp codeSign(String kid, SIG_FMT fmt, byte[] data) {
        logger.info("recv codeSign, kid:{}, data.len:{}", kid, data.length);
        if (IS_DEBUG) {
            return Resp.getFake_codeSign();
        }
        Map m = new HashMap<String, Object>() {
            {
                put("kid", kid);
                put("fmt", fmt.getFmt());
            }
        };

        //<editor-fold defaultstate="collapsed" desc="do hash">
        try {
            byte[] hash = null;
            if (SIG_FMT.isHashed(fmt)) {
                hash = data;
            } else {
                hash = CryptoTool.doHash(data);//SHA256
            }
            String hashStr = new String(Hex.encode(hash)).toUpperCase();
            logger.info("hashStr:{}", hashStr);
            m.put("hash", hashStr);
        } catch (Exception e) {
            return Resp.getFail(ERR.DO_HASH_FAIL);
        }
        //</editor-fold>

        Resp resp = toServer(SERVER_URL + "codeSign", m);

        //<editor-fold defaultstate="collapsed" desc="本地驗章">
//        try {
//            boolean rtn = CommonTool.verifyP1(CommonTool.der(resp.getSig()), SIG_FMT.isHashed(fmt) ? "1234".getBytes() : data, CommonTool.loadCertPemNoBegin(resp.getX5c().get(0)).getPublicKey());
//            logger.info("verifyP1 rtn: " + rtn);
//        } catch (Exception e) {
//            e.printStackTrace();
//        }
        //</editor-fold>
        //組P7
        if (SIG_FMT.P7 == fmt) {
            try {
                List<String> certs = resp.getX5c();
                byte[] p7 = CommonTool.buildP7withP1(certs.get(0), data, Base64.decode(resp.getSig()));//SHA256WithRSA
                String p7Str = new String(Base64.encode(p7));
                resp.setSig(p7Str);
            } catch (Exception e) {
                logger.error("buildP7withP1 fail", e);
                return Resp.getFail(ERR.BUILD_P7_FAIL);
            }
        }
        return resp;
    }

```
```
    public static void main(String[] args) throws Exception {
        Client client = Client.getInstance();
        try {

            String keyLabel = "test_20220531001";
//            logger.info(client.getVer().getVer());
//            logger.info(client.keyGenerate(keyLabel, ALG.ES256, LEN.LEN_256).getCode());
//            logger.info(client.keyDeactive(keyLabel).getCode());
//            logger.info(client.keyActive(keyLabel).getCode());
//            logger.info(client.getCertificate(keyLabel, CERT_FMT.SINGLE_CERT).getCode());
            logger.info(client.codeSign(keyLabel, SIG_FMT.P1, "1234".getBytes()).getSig());
//            logger.info(client.codeSign(keyLabel, SIG_FMT.P1_WITH_HASHED, CryptoTool.doHash("1234".getBytes())).getSig());
//            logger.info(client.codeSign(keyLabel, SIG_FMT.P7, "1234".getBytes()).getSig());
//            logger.info(client.listKey().getCode());

        } catch (Exception e) {
            logger.error("", e);
        }
    }
```
https://www.w3study.wiki/a/202109/1072497.html
## 8/20
* hash sandbox
    * dohash
    * hash傳送回得簽名
* sign sandbox
    * 得cert
    * 收hash 申請簽名

## 8/21
* sign sandbox
    * 得cert
    * 收hash 申請簽名
    * pe file
* sandbox架設起來
* a3.2測試報告
* a3.3測試報告
* pistis部屬
* siging flow
* sign hasg driver sandbox


https://stackoverflow.com/questions/41441276/how-to-decode-a-base64-encoded-certificate

https://stackoverflow.com/questions/41441276/how-to-decode-a-base64-encoded-certificate
```
    public static void main(String[] args) throws Exception {

        //****test
        Client twca_client = Client.getInstance();

        //****getver
        Resp ca_resp = twca_client.getVer();
        System.out.println("getVer: ");
        System.out.println(ca_resp.getCode());

        //****keygenerate -> kid、alg、len、pk、code、ts
        String uniqueID= UUID.randomUUID().toString().substring(0,16);
        Resp key_resp= twca_client.keyGenerate(uniqueID, ALG.RS256, LEN.LEN_2048);
        System.out.println("getGenerate: ");
        System.out.println(key_resp.getPk());

        //****keyActive
        //****keyDeactive

        //****keylist -> code, keyinfo, ts
        System.out.println("listKey: ");
        Resp keylist_resp = twca_client.listKey();
        System.out.println(keylist_resp.getCode());

        if (keylist_resp.getCode().compareTo("0") != 0){
            System.out.println("listKey FAIL ");
        }
        else{
            StringBuilder result = new StringBuilder("{\"key\":[");
            List<Resp.KeyInfo> keys = keylist_resp.getKeyInfo();
            System.out.println("keys number");
            System.out.println(keys.size());
            for(int i = 0 ; i< keys.size() ; i++){
                if (i==0){
                    result.append("{\"kid\":").append(keys.get(i).getKid())
                            .append(",\"active\":").append(keys.get(i).getStatus()== 0 ? "false" : "true")
                            .append("}");
                }
                else{
                    result.append(",{\"kid\":").append(keys.get(i).getKid()).append("\"")
                            .append(",\"active\":").append(keys.get(i).getStatus()== 0 ? "false" : "true")
                            .append("}");
                }
            }
            result.append("]}");
            //System.out.println(keylist_resp.getCode());
            System.out.println(result);
            //return;

            //****getCertificate -> code, kid, ts, x5c
            System.out.println("getCertificate: ");
            //JSONObject jo = new JSONObject()
            CERT_FMT cert_type=CERT_FMT.SINGLE_CERT;//CERTCHAIN
            String kid = "fe_prod_soft";
            Resp b64code_cert_resp = twca_client.getCertificate(kid, cert_type);
            System.out.println(b64code_cert_resp.getX5c());

        }
    }
```



* meeting
    * A3.1分三個說明書
        * fECP安裝操作說明書
        * 容器化部屬說明書
        * 可信運算說明書
    * A3.2 overview重新撰寫
        a.	將TWCA頒發的X.509公鑰證書安裝到由TWCA認證的客戶端和伺服器上
        b.	在這些經過認證的客戶端和伺服器上安裝這些交易模組
        c.	在這些通過認證的客戶端和伺服器之間執行這些交易的操作程序
        d.	確保這些交易的機密性、完整性、真實性和不可否認性的測試程序
    * 

