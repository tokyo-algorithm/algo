# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

row = 5
column = 8

for i in range(1, row+1):
	for j in range(column-i):
		print('0', end='')
	for j in range(1, i+1):
		print(j, end='')
	print()