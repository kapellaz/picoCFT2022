#!/usr/bin/env python3


import string

flag=[]

with open("message.txt") as f:
	contents = f.read()
	n = [int(v) for v in contents.split()]
	for i in n:
		modulo = pow(i,-1,41)
		if modulo in range(1,27):
			flag.append(string.ascii_uppercase[modulo-1])
		elif modulo in range(27,37):
			flag.append(string.digits[modulo-27])
		else:
			flag.append("_")


print("picoCTF{%s}" % "".join(flag))
