@echo off

set domain=%1
set ip=%2
set port=%3
if %3 == 80 (set protocol=http://)
if %3 == 443 (set protocol=https://)
set url=%protocol%%domain%
set basetitle=curl - %domain%解析为%ip%

title %basetitle%

echo curl %ip%网站访问测试
echo 在本测试中，我们会以访问%domain%的名义尝试访问服务器%ip%。URL为%url%，其中%domain%被解析为%ip%。
echo 请按下任意键测试一次
pause

:curl
title %basetitle% - 请求中

.\curl.exe -I -k -v --resolve %domain%:%port%:%ip% %url%
set lastreturn=%errorlevel%

title %basetitle% - 请求结束

if %lastreturn% == 0 (echo 请求成功) else (echo 请求失败)

echo 请按下任意键再测试一次
pause

goto curl
