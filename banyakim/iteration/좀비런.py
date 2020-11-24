# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

'''
count = int(input().strip())
number_list = list(int(input()) for _ in range(count))
print(number_list)
'''

zom_count = int(input())
zom_speed = list(map(int, input().split()))
max_speed = 0

for i in zom_speed:
	if i >= max_speed:
		max_speed = i
print(max_speed)


