#!/usr/bin/env python3
import sys

def write(num):
	with open("/proc/sys/kernel/randomize_va_space", "w") as f:
		f.write(num)
		f.close()

def read():
	f = open("/proc/sys/kernel/randomize_va_space", "r")
	if int(f.read()) == 0:
		return True
	else:
		return False
def banner():
	banner = ('''
Usage:
aslr [integer]
aslr [check]
''')
	return banner

if __name__ == "__main__":
	try:
		if len(sys.argv) != 2:
			print(banner())
		elif sys.argv[1] == "check":
			if read() == True:
				print("Aslr is disabled")
			else:
				print("Aslr is enabled")
		else:
			write(sys.argv[1])
	except:
		print(banner())
