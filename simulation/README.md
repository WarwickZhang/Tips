**本文主要讲述Mac系统的配置方法，windows请移步[使用windows系统配置iOS模拟定位](http://www.feng.com/iPhone/news/2016-11-03/Feng-friends-sharing-iOS-7910-escape-can-not-virtual-location_661010.shtml)**

### 工具:

- iPhone
- iTunes

### 具体步骤：

涉及iTunes的备份和还原，目前已知可能会造成微信、微博、支付宝等App登录信息丢失。**请不要自己一个人在家的时候玩**。

手机连接电脑，打开iTunes。选择`备份`->`本电脑`->`立即备份` 

进度条完成后，打开` ~/Library/Application\ Support/MobileSync/Backup`，搜索里面的`e3722676133184621303a00be5f4ce1714c57695`文件，替换成[e3722676133184621303a00be5f4ce1714c57695]。

再次打开iTunes。选择`备份`->`本电脑`->`恢复备份` 。等待完成，自动重启手机，完成。