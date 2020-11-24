# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
count = int(input())
numbers= list(map(int,input().split()))
# a,b,c = map(int,input().split()) 

print(min(numbers))


'''
min = numbers[0]

for num in numbers:
	if num < min:
		min = num
print(min)
'''
