# Charles规则配置

### 背景

开发的App中一部分请求开启了本地证书校验，使Charles默认的ssl证书无效。从而导致在使用charles抓包时一些接口不通，有的还是关键接口，此时就必须改代码/关代理才能走通流程，影响开发和测试的效率。

**那么是否可以让那些接口绕过charles呢？**

查阅Charles官方文档，发现在手机端配置代理时，不仅可以用手动配置，也可以用自动配置 [charlesproxy](https://www.charlesproxy.com/documentation/configuration/browser-and-system-configuration/)

实际上是chls.pro服务返回一个.pac文件，通过.pac文件自动配置。那么我自己写一个pac是不是就可以满足QA的需求了呢？

查阅pac文件相关[文档](http://www.cisco.com/c/en/us/td/docs/security/web_security/connector/connector2972/PACAP.html) 写了个pac文件，自己再搭个[python](https://docs.python.org/2/library/simplehttpserver.html)本地服务器，搞定。



### 详细步骤

##### 1.编写PAC文件

pac使用javascript语言，只要实现`FindProxyForURL`即可。

以下代码为`m.baidu.com` 域名下的直连，其他的走代理

```javascript
function FindProxyForURL(url, host) {
  if (host=="m.baidu.com") {
    return 'DIRECT;';
  }
  return 'PROXY <your ip address>:8888;';
}
```

新建`~/pac`目录  保存到`~/pac/chls.pac`

##### 2.启动python服务

`cd ~/pac;python -m SimpleHTTPServer  `

可以在本地打开http://localhost:8000 测试一下

##### 3.链接代理

设置->无线局域网->打开你连接的Wi-Fi->HTTP代理->自动

输入`http://<your ip address>:8000/chls.pac`

##### 4.enjoy it!😄


**当然，你也可以把配置放在远程服务器上，本地写一个同步ip的[脚本](https://github.com/WarwickZhang/Tips/blob/master/charles/upload.py)**
