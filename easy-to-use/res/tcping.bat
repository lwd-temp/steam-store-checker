@echo off

set ip=%1
set port=%2
set basetitle=tcping - %ip%:%port%

title %basetitle%

echo �ڱ������У����ǻ᲻�ϲ���%ip%:%port%�Ƿ�ɴ�����ɴ�����ʾ��No Response����

.\tcping.exe -t %ip% %port%

pause