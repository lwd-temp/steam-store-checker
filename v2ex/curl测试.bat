@echo off
title curl测试
echo 请按下任意键测试一次
pause
:curl
title curl测试 - 请求中
curl -I -k -v --resolve store.steampowered.com:443:23.42.182.65 https://store.steampowered.com
title curl测试 - 请求结束
echo 执行结束
echo 请按下任意键再测试一次
pause
goto curl
