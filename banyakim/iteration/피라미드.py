# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

num = int(input())

for i in range(1, num+1):
	for j in range(num-i):
		print(' ', end='')
	for j in range(2*i - 1):
		print('*', end='')
	print()
	
'''
다른풀이
for i in range(1, num+1):
	for j in range(num-i):
		print(' ', end='')
	for j in range(1, i*2, 1):
		print('*', end='')
	print('')
'''