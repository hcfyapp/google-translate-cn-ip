# google-translate-cn-ip

自 2022 年 9 月 28 日起，谷歌翻译退出了中国市场，这导致 `translate.googleapis.com` 这个谷歌翻译接口域名无法在国内直接连通，但目前可以通过修改 hosts 的方式从国内连接到此域名。

此项目的目的是收集可以从国内直接访问 `translate.googleapis.com` 的 IP 地址（后文简称为“可用 IP”），欢迎大家提供可用 IP。

## 可用 IP 列表

你可以通过以下链接读取到这个文件的最新内容：

https://raw.githubusercontent.com/hcfyapp/google-translate-cn-ip/main/ips.txt

## 如何测试 IP 是否可用

1. 从 ips.txt 中选择一个 IP，例如 `142.250.4.90`。
2. 跟 `translate.googleapis.com` 组成一条 hosts 规则，例如 `142.250.4.90 translate.googleapis.com`，注意 IP 地址后面有一个空格。
3. 修改电脑里的 hosts 文件，将这条规则粘贴到 hosts 文件的最后一行。修改 hosts 文件的方法请参考[这条链接里的“手动修改”方案](https://hcfy.app/blog/2022/09/28/ggg)。
4. **重启浏览器**之后，按照第 3 步中的链接的“测试谷歌翻译是否恢复正常”来判断此 IP 是否可用。

## 更新日志

从以下两个来源整理了第一份 ips.txt：

- https://github.com/hcfyapp/crx-selection-translate/discussions/1526#discussioncomment-3956157
- https://www.v2ex.com/t/888970#r_12246970
