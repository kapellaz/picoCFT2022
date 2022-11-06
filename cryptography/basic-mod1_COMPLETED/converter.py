#!/usr/bin/env python3


import string


with open("message.txt") as f:
	contents = f.read()
	n = [int(v) for v in contents.split()]
	for i in n:
		modulo = i % 37
		if modulo in range(26):
			print(string.ascii_uppercase[modulo],end="")
		elif modulo in range(26,36):
			print(string.digits[modulo-26],end="")
		else:
			print("_",end="")
