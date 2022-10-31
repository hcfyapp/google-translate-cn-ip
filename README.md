# google-translate-cn-ip

自 2022 年 9 月 28 日起，谷歌翻译退出了中国市场，这导致 `translate.googleapis.com` 这个谷歌翻译接口域名无法在国内直接连通，但目前可以通过修改 hosts 的方式从国内连接到此域名。

此项目的目的是收集可以从国内直接访问 `translate.googleapis.com` 的 IP 地址（后文简称为“可用 IP”），欢迎大家提供可用 IP。

## 可用 IP 列表

你可以通过以下链接读取到这个文件的最新内容：

https://raw.githubusercontent.com/hcfyapp/google-translate-cn-ip/main/ips.txt

## 如何使用以及测试 IP 是否可用

见 https://hcfy.app/blog/2022/09/28/ggg 中的【修改 hosts / IP 方案】。

## 其它工具

### 集扫描可用 IP + 测速 + 自动写入 hosts 于一体的工具

@Ponderfly 开发了一个工具，项目主页：https://github.com/Ponderfly/GoogleTranslateIpCheck

大家可以去试用一下。

## 其它资源

### 获取可用 IP 的方法

v2ex 上有个老哥提供了一个方法，但我不懂 go，这位老哥也没有写文档，我把这位老哥分享的方法写在下方，希望有个大佬能提供一份使用文档。

来源：https://www.v2ex.com/t/888970#r_12246970

> 只要是 GWS 服务器都可以，可以扫描出来。
> 用的是 gscan_quic ，我开了这个分支。文档还没写。
> 原 repo: https://github.com/Kisesy/gscan_quic
> Frok: https://repo.or.cz/gscan_quic.git

@yjd 有提供使用方法：https://github.com/hcfyapp/crx-selection-translate/discussions/1526#discussioncomment-3962409

但是粗略看下来我还是有些细节不太明白，最好能润色成一篇非技术人员也看得懂的文档存放在此仓库中。

## 更新日志

请查看 CHANGELOG.md 文件。
