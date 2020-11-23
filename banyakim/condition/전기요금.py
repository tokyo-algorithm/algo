# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
used = int(input())
fee = 0
unit = 2
under_100 = 0.005
under_200 = 0.007
under_300 = 0.009
over_300 = 0.01

#if used < 0:
#	return
if used < 100:
	fee = used * under_100
elif used < 200:
	fee = used * under_200
elif used < 300:
	fee = used * under_300
else:
	fee = used * over_300

print(format(fee, '.2f'))
s