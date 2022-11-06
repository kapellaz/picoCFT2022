decode="VOUHMJLTESZCDKWIXNQYFAPGBR"
encode="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

txt = str(input())


for i in txt.upper():
	if i in decode:
		index = decode.index(i)
		print(encode[index], end="")
	else:
		print(i, end="")
