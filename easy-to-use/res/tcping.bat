@echo off

set ip=%1
set port=%2
set basetitle=tcping - %ip%:%port%

title %basetitle%

echo 在本测试中，我们会不断测试%ip%:%port%是否可达。若不可达，则会提示“No Response”。

.\tcping.exe -t %ip% %port%

pause