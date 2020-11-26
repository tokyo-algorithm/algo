# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

num1, num2 = map(int, input().split(' '));
# print(num1, num2)

def min(num1, num2):
	if num1 > num2:
		print(num2)
	elif num1 < num2:
		print(num1)
	else:
		print('cannot calculate!')

min(num1, num2)