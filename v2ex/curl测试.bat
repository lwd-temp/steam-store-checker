@echo off
title curl����
echo �밴�����������һ��
pause
:curl
title curl���� - ������
curl -I -k --resolve store.steampowered.com:443:23.42.182.65 https://store.steampowered.com
title curl���� - �������
echo ִ�н���
echo �밴��������ٲ���һ��
pause
goto curl
