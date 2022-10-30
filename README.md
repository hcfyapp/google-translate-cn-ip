# google-translate-cn-ip

自 2022 年 9 月 28 日起，谷歌翻译退出了中国市场，这导致 `translate.googleapis.com` 这个谷歌翻译接口域名无法在国内直接连通，但目前可以通过修改 hosts 的方式从国内连接到此域名。

此项目的目的是收集可以从国内直接访问 `translate.googleapis.com` 的 IP 地址（后文简称为“可用 IP”），欢迎大家提供可用 IP。

## 可用 IP 列表

你可以通过以下链接读取到这个文件的最新内容：

https://raw.githubusercontent.com/hcfyapp/google-translate-cn-ip/main/ips.txt

## 如何测试 IP 是否可用

### 手动测试

1. 从 ips.txt 中选择一个 IP，例如 `142.250.4.90`。
2. 跟 `translate.googleapis.com` 组成一条 hosts 规则，例如 `142.250.4.90 translate.googleapis.com`，注意 IP 地址后面有一个空格。
3. 修改电脑里的 hosts 文件，将这条规则粘贴到 hosts 文件的最后一行。修改 hosts 文件的方法请参考[这条链接里的“手动修改”方案](https://hcfy.app/blog/2022/09/28/ggg)。
4. **重启浏览器**之后，按照第 3 步中的链接的“测试谷歌翻译是否恢复正常”来判断此 IP 是否可用。

### 自动测试

使用 `checker.py` 可以自动化测试出响应速度最快的 5 个 IP 地址。

```bash
# 使用代码内置的 IP 库
check

# 也可以自定义需要测速的 IP 库，将需要测试的 IP 库写进 ips.txt 即可，格式为每行一个 IP
check ips.txt
```

## 需要解决的问题

### 需要一个可以获取可用 IP 的方法

目前的可用 IP 来自网络上网友提供，但我们最好是能有一个可以自行获取到可用 IP 的方法。

v2ex 上有个老哥提供了一个方法，但我不懂 go，这位老哥也没有写文档，我把这位老哥分享的方法写在下方，希望有个大佬能提供一份使用文档。

来源：https://www.v2ex.com/t/888970#r_12246970

> 只要是 GWS 服务器都可以，可以扫描出来。
> 用的是 gscan_quic ，我开了这个分支。文档还没写。
> 原 repo: https://github.com/Kisesy/gscan_quic
> Frok: https://repo.or.cz/gscan_quic.git

@yjd 有提供使用方法：https://github.com/hcfyapp/crx-selection-translate/discussions/1526#discussioncomment-3962409

但是粗略看下来我还是有些细节不太明白，最好能润色成一篇非技术人员也看得懂的文档存放在此仓库中。

### 需要一个测试 ips.txt 里哪些 ip 可以用且按照速度排序的程序

@GoodCoder666 在这里提供了[一段 python 代码用于测速](https://github.com/hcfyapp/crx-selection-translate/discussions/1526#discussioncomment-3956176)，且[提供了打包好的 .exe 文件](https://github.com/hcfyapp/crx-selection-translate/discussions/1526#discussioncomment-3956177)可以直接运行。

我觉得可以做以下改进：

1. 代码可以改为默认从使用此仓库的 ips.txt 链接获取
2. 目前只提供了 .exe 的执行程序，最好能提供一个 macOS 也能运行的执行程序

### 最终目标：一个获取可用 IP + 测速 + 写入 hosts 的程序

获取可用 IP 可能需要长时间运行，可以不放在程序中，但测速 + 写入 hosts 应该是能做在同一个程序里的。

## 更新日志

请查看 CHANGELOG.md 文件。
