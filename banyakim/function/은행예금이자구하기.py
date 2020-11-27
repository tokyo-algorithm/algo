# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

principal, rate, year = map(float, input().split(' '))
year = int(year)
	
def cal_compound_interest(principal, rate, year):
	total = 1
	
	for i in range(1, year+1):
		total *= (1 + rate/100)
		# print(total)
	print("%.2f" %(principal * total))
		
cal_compound_interest(principal, rate, year)