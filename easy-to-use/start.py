# Easy-to-use-Steam-Store-Checker Launcher Script
# Author: lwd-temp
import os
import socket
import sys

if os.name != "nt":
    print("请在Windows系统中运行本程序。")
    sys.exit()

steamStoreDomain = "store.steampowered.com"
hkGovDomain = "www.gov.hk"
helpText = """概念解读：
当我们访问一个网站时，我们事实上连接了那个网站的服务器。
IP地址用于标记服务器“位置”，而端口用于标记服务器的服务。
80端口通常用于HTTP协议（“未加密的网页”），而443端口通常用于HTTPS协议（“加密的网页”）。
TLS协议是网络通讯的安全基础（被HTTPS协议所采用）。TLS提供的认证加密使得用户可以确定他们在与谁通讯， 并确保通讯信息不被中间人看到或篡改。
虽然TLS可以隐藏用户通讯的内容，但其并不能总是隐藏与用户通讯的对象。
比如TLS握手可以携带一个叫做加密服务器名称指示（SNI）的扩展, 这个扩展帮助客户端告诉服务器其想要访问的网站的域名。
不幸的是，由于协议的历史遗留问题，SNI是未被加密的，这使得中间人可以获取我们访问的服务器域名。
这里的“中间人”可以是您的路由器、互联网服务商（ISP）、学校或企业网络管理员或政府。
一个服务器可以同时为多个域名提供服务，它们通过请求中的SNI扩展来区分。

举例分析：
本例中，服务器域名为store.steampowered.com，端口为443。中间人通过SNI判断并阻止了您的访问。
由于我们可以在连接服务器时“假装”访问任何域名，我们可以通过观察以Steam商店“名义”访问无关境外服务器是否也被阻止来判断中间人是否针对store.steampowered.com发起攻击。

备注：
您也可以通过Linux下的traceroute工具来查看您被哪个设施阻止了访问（TCP连接，443端口），这样便可以排除Steam商店主动拒绝的可能。

无关紧要的引言：
用伤害无辜者来掩盖自己的错误是心虚的体现，也永远掩盖不了。他们也一样。（汉娜 梅）
"""


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
        base_path = os.path.join(os.path.abspath("."), "res")
    return base_path


def queryDNS(domain):
    return socket.gethostbyname(domain)


def callCurlBat(domain, ip, port):
    os.system("start cmd curl.bat " + str(domain) +
              " " + str(ip) + " " + str(port))


def callTcpingBat(ip, port):
    os.system("start cmd tcping.bat " + str(ip) + " " + str(port))


def printHorizontalLine():
    print("-" * 10)


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
    printHorizontalLine()
    print("请在新窗口中获取帮助及操作。")
    input("按回车键回到主菜单...")
    printHorizontalLine()
    main()


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
    printHorizontalLine()
    print("请在新窗口中获取帮助及操作。")
    input("按回车键回到主菜单...")
    printHorizontalLine()
    main()


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
    printHorizontalLine()
    print("请在新窗口中获取帮助及操作。")
    input("按回车键回到主菜单...")
    printHorizontalLine()
    main()


def help():
    print(helpText)
    input("按回车键回到主菜单...")
    printHorizontalLine()
    main()


def main():
    print("store.steampowered.com连接测试工具包启动器")
    print("工作目录：" + os.getcwd())
    printHorizontalLine()
    print("请选择操作：")
    print("[1]常规访问store.steampowered.com")
    print("[2]访问store.steampowered.com，但将其IP解析为香港特别行政区政府官网服务器")
    print("[3]访问fuck.steampowered.com，但将其IP解析为Steam商店服务器")
    print("[4]帮助")
    print("[5]退出")
    print("注：所有访问均使用443端口。")

    while True:
        try:
            choice = int(input("请输入对应数字并按Enter键继续："))
            if choice == 1:
                printHorizontalLine()
                stdConn()
                break
            elif choice == 2:
                printHorizontalLine()
                hkConn()
                break
            elif choice == 3:
                printHorizontalLine()
                fuckConn()
                break
            elif choice == 4:
                printHorizontalLine()
                help()
                break
            elif choice == 5:
                printHorizontalLine()
                sys.exit()
            else:
                print("输入错误，请重新输入")
                continue
        except ValueError:
            print("输入错误，请重新输入")
            continue


if __name__ == '__main__':
    os.chdir(getWorkDir())
    os.system("title store.steampowered.com连接测试")
    main()
