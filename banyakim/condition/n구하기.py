# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())
sum = 0;

for i in range(1, user_input+1):
	sum += i
	if sum > user_input:
		print(i)
		break

