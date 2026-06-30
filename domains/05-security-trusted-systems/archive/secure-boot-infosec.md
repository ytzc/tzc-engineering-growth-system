# Secure Boot Infosec

## 8/14
* 第4章
* mender-convert
    * 2 rootfs
    * bootloader 
        * 2選1
        * Mender client 
        * configure
    * 輸出
        * converted image
        * 遠端的Mender Artifact
        * ext4 image 檔案格式
## 5/16
* 了解harbor, notary 關係畫圖
* 走預設notary 完成駭客測試
    * https://github.com/zj1244/Blog/blob/master/2019/harbor%E7%9A%84Notary%E5%8A%9F%E8%83%BD%E6%B5%8B%E8%AF%95.md





* 驗證signer(Ok)
* harbor config singer
* secure boot情境
* init script
* demo
* manifest

## 以下筆記

sudo BOARDID=3448 BOARDSKU=0002 FAB=400 FUSELEVEL=fuselevel_production  ./nvmassfusegen.sh -j -i 0x21 --auth NS -p -k <key.pem>  jetson-nano-devkit-emmc
wsl 安裝
https://developer.aliyun.com/article/1076324

https://forums.developer.nvidia.com/t/sdk-manager-ubuntu-20-04-lts/125711/39
```


docker run -it --rm sdkmanager --cli install --logintype devzone --product jetson --host --targetos Linux --version 4.6.2 --target JETSON_NANO_TARGETS --select 'Jetson OS' --select 'Jetson SDK Components' --flash skip

#setup nvidia sdk manager
sudo apt update
sudo apt install ./sdkmanager_1.9.0-10816_amd64.deb -y
sdkmanager --ver

sdkmanager --cli install --logintype devzone --product jetson --host --targetos Linux --version 4.6.2 --target JETSON_NANO_TARGETS --select 'Jetson OS' --select 'Jetson SDK Components' --flash skip

```
### 8221
* massfuse



## 11/30
* fuse ~1600
* restful ~1700
* code sign service ~2000
# 11/23
* 安裝 Secure Boot package
* <DK_file>
    * A 32-bit number / big-endian HEX format.
    * 應用加密
* <SBK_file> 
    * 不會加密bootloader
    * pkc_disable = 0
    * 應用加密
* PKC
    * 私鑰
*  PKC HASH 
* burn
* sign
* flash

## 11/8
* nano secure boot
* codesign
* 
## 11/7
* nano secure boot
* codesign
* python script
## 11/2
* fecp需求性
* secure boot要怎麼走




* 架構圖
    * 步驟 簡單淺顯易懂 (security) 達到的效果 素材
    * 給嘉宏跟cris
    * 明天下午 嘉宏 ricky cris
    * 架構圖 步驟 效果
* device certificate
* 細一點素材

* portainer

```
teamviewer
4t1mt87e
```

* x11
```

Xming X Server for Windows
我个人喜欢的是VcXsrv这个X11 Server，可以在这里下载它的安装包。

安装好以后，打开桌面上的XLaunch，然后选择Multiple windows->Start no client->勾选Disable access control->Save Configuration保存一下设置，方便以后使用->Finish。

export DISPLAY="grep nameserver /etc/resolv.conf | sed 's/nameserver //':0.0"
"grep nameserver /etc/resolv.conf | sed 's/nameserver //':0"
grep nameserver /etc/resolv.conf | sed 's/nameserver //'
```
## 9/6
* 6450 
    * driver 
    * update bios
    * kernel
    * secure boot
        * sign kernel
* ubuntu 20.04.4LTS
    * linux kernel: 5.10.0-1057-oem
* let's encrypt
* test pod
* diagram
## 9/4
* capability~00
    * grpcurl 呼叫成功
* 6450 kernel ~0030
    * https://packages.ubuntu.com/focal/amd64/linux-image-5.10.0-1057-oem/download
    * ubuntu 20.04.4LTS
    * linux kernel: 5.10.0-1057-oem
    * driver

* 6450 pistis
* driver
* 畫圖
## 9/1
* 6450 kernel
    * https://packages.ubuntu.com/focal/amd64/linux-image-5.10.0-1057-oem/download
    * ubuntu 20.04.4LTS
    * linux kernel: 5.10.0-1057-oem
    * driver
* capability
* 6450 pistis
* email
* 運動
## 8/31
* 6450 kernel
    * https://packages.ubuntu.com/focal/amd64/linux-image-5.10.0-1057-oem/download
    * ubuntu 20.04.4LTS
    * linux kernel: 5.10.0-1057-oem
* capability
* 6450 pistis
* email
* 運動

### Note
https://b8807053.pixnet.net/blog/post/347445314-ubuntu-update-kernel
```
 sudo apt-cache search linux-image-* | grep 5.10.0-1057
 
 sudo apt-get install linux-image-5.10.0-1057-oem
 
 sudo update-initramfs -u -k all
 sudo update-grub
 sudo reboot
 
```
```
https://blog.ladsai.com/ubuntu-%E5%88%87%E6%8F%9B-kernel-%E7%89%88%E6%9C%AC.html

https://packages.ubuntu.com/focal/linux-image-5.10.0-1057-oem

uname -r 
5.10.0-1057-oem

dpkg -i *.deb
```
## 8/30
* block diagram
    * UML
        * use case diagram
        * activity diagram
        * sequence diagram
        * file server(是否需要)
* secure boot nano
* device key nano
* capability api
* OVA
# 8/29
* 數位憑證技術與應用, Spring Boot, 隱私計算



## 8/28
* jar包裝 ~1830
* container傳檔案 ~1900
* secure boot錄影 ~1930
* 錄影五分鐘 ~2000
## 8/24
* secure boot
* 重新佈署pistis 



## 8/18
* ubuntu20.04.2 linux kernel安裝
    * secure boot mok
* pistis部屬
* mok burning
* 可信執行環境pdf
* siging flow
* sign hasg driver sandbox

