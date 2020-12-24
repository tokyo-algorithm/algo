# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()

ret = user_input[::-1]

for index in range(len(user_input)):
	if ret[index] == "0":
		continue
	else:
		print(ret[index:])
		break
