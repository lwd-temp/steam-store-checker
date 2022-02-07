import os
import socket
import sys

if os.name != "nt":
    print("请在Windows系统中运行本程序。")
    sys.exit()

steamStoreDomain = "store.steampowered.com"
hkGovDomain = "www.gov.hk"


def resource_path(relative_path):
    if getattr(sys, 'frozen', False):  # 是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def getWorkDir():
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return base_path


def queryDNS(domain):
    return socket.gethostbyname(domain)


def callCurlBat(domain, ip, port):
    os.system("start curl.bat " + str(domain) +
              " " + str(ip) + " " + str(port))


def callTcpingBat(ip, port):
    os.system("start tcping.bat " + str(ip) + " " + str(port))


def stdConn():
    print("常规访问store.steampowered.com")
    print("解析Steam商店域名...")
    steamStoreIP = queryDNS(steamStoreDomain)
    print(steamStoreIP)
    print("唤起Tcping80端口测试脚本...")
    callTcpingBat(steamStoreIP, 80)
    print("唤起Tcping443端口测试脚本...")
    callTcpingBat(steamStoreIP, 443)
    print("唤起Curl测试脚本...")
    callCurlBat(steamStoreDomain, steamStoreIP, 443)
    print("请在新窗口中获取帮助及操作。")
    input("按回车键关闭此窗口...")
    sys.exit()


def hkConn():
    print("访问store.steampowered.com，但将其IP解析为香港特别行政区政府官网服务器")
    print("解析香港特别行政区政府官网域名...")
    hkGovIP = queryDNS(hkGovDomain)
    print(hkGovIP)
    print("唤起Tcping80端口测试脚本...")
    callTcpingBat(hkGovIP, 80)
    print("唤起Tcping443端口测试脚本...")
    callTcpingBat(hkGovIP, 443)
    print("唤起Curl测试脚本...")
    callCurlBat(steamStoreDomain, hkGovIP, 443)
    print("请在新窗口中获取帮助及操作。")
    input("按回车键关闭此窗口...")
    sys.exit()


def fuckConn():
    print("访问fuck.steampowered.com，但将其IP解析为Steam商店服务器")
    print("解析Steam商店域名...")
    steamStoreIP = queryDNS(steamStoreDomain)
    print(steamStoreIP)
    print("唤起Tcping80端口测试脚本...")
    callTcpingBat(steamStoreIP, 80)
    print("唤起Tcping443端口测试脚本...")
    callTcpingBat(steamStoreIP, 443)
    print("唤起Curl测试脚本...")
    callCurlBat("fuck.steampowered.com", steamStoreIP, 443)
    print("请在新窗口中获取帮助及操作。")
    input("按回车键关闭此窗口...")
    sys.exit()


os.chdir(getWorkDir())
print("store.steampowered.com连接测试")
print("工作目录：" + os.getcwd())
print("\n")
print("请选择操作：")
print("[1]常规访问store.steampowered.com")
print("[2]访问store.steampowered.com，但将其IP解析为香港特别行政区政府官网服务器")
print("[3]访问fuck.steampowered.com，但将其IP解析为Steam商店服务器")
print("注：所有访问均使用443端口。")

while True:
    try:
        choice = int(input("请输入对应数字并按Enter键继续："))
        if choice == 1:
            stdConn()
            break
        elif choice == 2:
            hkConn()
            break
        elif choice == 3:
            fuckConn()
            break
        else:
            print("输入错误，请重新输入")
            continue
    except ValueError:
        print("输入错误，请重新输入")
        continue
