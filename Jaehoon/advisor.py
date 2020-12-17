# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
num1 = int(input())

def divide():
	for i in range(1, num1):
		if(num1 % i) == 0:
			divisor = num1 / i
			print ("%10s"% (divisor))

			
if __name__ == '__main__':
	divide()