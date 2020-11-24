# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
input_number = input()
num = int(input_number)

if num <= 20:
	for i in range (1, num+1):
		for j in range (1, num+1):
			print(i, end=' ')
			i = i+num
		print()

