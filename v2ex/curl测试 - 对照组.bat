@echo off
title curl���� - ������
echo �밴�����������һ��
pause
:curl
title curl���� - ������ - ������
curl -I -k -v --resolve store.steampowered.com:443:34.227.211.26 https://store.steampowered.com
title curl���� - ������ - �������
echo ִ�н���
echo �밴��������ٲ���һ��
pause
goto curl
