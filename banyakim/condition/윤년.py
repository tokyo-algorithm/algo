# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
leap_year = 'Leap Year'
not_leap_year = 'Not Leap Year'

user_input = int(input())

if user_input % 400 is 0:
	print (leap_year)
elif user_input % 100 is 0:
	print(not_leap_year)
elif user_input % 4 is 0:
	print (leap_year)
else:
	print(not_leap_year)
	
	