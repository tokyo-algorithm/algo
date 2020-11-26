# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

a, b, c, d = map(int, input().split(' '))

def mul(a, b):
	return a * b

print(mul(mul(a, b), mul(c, d)))