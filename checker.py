# -*- coding: utf-8 -*-
from urllib.request import Request, urlopen
from sys import stdout, argv
from time import time

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'sec-ch-ua': '"Chromium";v="106", "Not;A=Brand";v="99", "Google Chrome";v="106.0.5249.119"',
    'host': 'translate.googleapis.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
}

def check_ip(ip):
    url = f'http://{ip}/translate_a/single?client=gtx&sl=en&tl=fr&q=a'
    try:
        start_time = time()
        response = urlopen(Request(url, headers=HEADERS), timeout=3)
        end_time = time()
        response.close()
    except Exception as e:
        return str(e)
    return end_time - start_time

if len(argv) == 1:
    ips = ['108.177.122.90', '142.250.0.90', '142.250.10.90', '142.250.100.90', '142.250.101.90', '142.250.105.90', '142.250.107.90', '142.250.11.90', '142.250.110.90', '142.250.111.90', '142.250.112.90', '142.250.12.90', '142.250.125.90', '142.250.126.90', '142.250.128.90', '142.250.136.90', '142.250.185.174', '142.250.185.238', '142.250.189.206', '142.250.203.142', '142.250.218.14', '142.250.27.90', '142.250.28.90', '142.250.30.90', '142.250.31.90', '142.250.4.90', '142.250.8.90', '142.250.9.90', '142.250.96.90', '142.250.97.90', '142.250.98.90', '142.251.10.138', '142.251.116.101', '142.251.40.174', '142.251.5.90', '142.251.9.90', '172.217.0.46', '172.217.13.142', '172.217.16.46', '172.217.192.90', '172.217.195.90', '172.217.203.90', '172.217.204.90', '172.217.214.90', '172.217.215.90', '172.217.222.90', '172.217.31.142', '172.253.112.90', '172.253.114.90', '172.253.115.90', '172.253.116.90', '172.253.122.90', '172.253.123.90', '172.253.124.90', '172.253.126.90', '172.253.62.90', '216.58.209.174', '216.58.214.14', '216.58.220.142']
else:
    try:
        with open(argv[1], 'r') as file:
            ips = list(map(str.strip, file))
    except Exception as e:
        print(f'Failed to open file {argv[1]}. Reason: {e}')

avaliable = []
for ip in ips:
    print(f'Checking {ip} ...', end=' ')
    stdout.flush()
    result = check_ip(ip)
    if isinstance(result, str):
        print('Error:', result)
    else:
        ms = round(result * 1000)
        print(f'{ms}ms')
        avaliable.append((ms, ip))

avaliable.sort()
top5 = avaliable[:5]

print('\n响应速度前5的IP:')
for ms, ip in top5:
    print(f'{ip}:\t{ms}ms')

print('\nHOSTS 添加内容：')
for ms, ip in top5:
    print(ip, 'translate.googleapis.com')