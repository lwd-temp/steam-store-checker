@echo off
title curl测试 - 对照组
echo 请按下任意键测试一次
pause
:curl
title curl测试 - 对照组 - 请求中
curl -I -k --resolve store.steampowered.com:443:34.227.211.26 https://store.steampowered.com
title curl测试 - 对照组 - 请求结束
echo 执行结束
echo 请按下任意键再测试一次
pause
goto curl
