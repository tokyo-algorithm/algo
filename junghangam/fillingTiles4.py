# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
# print ("Hello Goorm! Your input is " + user_input)
inputs = user_input.split(" ")

cur = [1,3]

if int(inputs[0]) < 3:
	print(cur[int(inputs[0])])
else:
	for i in range(2, int(inputs[0])):
		cur.append(cur[i-1] + cur[i-2]*2)

	print(cur[-1] % int(inputs[1]))
