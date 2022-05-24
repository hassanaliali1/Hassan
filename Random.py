import platform
import os
os.system('termux-setup-storage')
arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("none").Main()
elif 'aarch' in arc:
	__import__("Hasan").Main()
else:
	exit(f' Unknow device machine {arc}')
