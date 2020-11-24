# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
num = int(input())

for i in range(num):
	for j in range(num - i):
		print('*', end='')
	print()

