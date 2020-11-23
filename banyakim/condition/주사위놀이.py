# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
num = int(input())
dice = 6
if not(num >= 2 or num <= 12):
	print('input a number greater than 2 and less than 12')

for i in range(1, dice + 1):
	for j in range(1, dice + 1):
		if i + j is num:
			print(i, j)

