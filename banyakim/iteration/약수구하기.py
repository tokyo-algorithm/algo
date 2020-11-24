# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
num = int(input())
result = []

for i in range(1, num + 1):
	if num % i is 0:
		print(i, end=' ')

