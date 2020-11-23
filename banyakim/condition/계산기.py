def plus(a, b):
	return a + b

def minus(a, b):
	return a - b

def multiple(a, b):
	return a * b

def divide(a, b):
	return format(a / b, '.2f') 

user_input = input()
list = user_input.split(' ')
# print(list)

type = list[1]
first_num = int(list[0])
second_num = int(list[2])
result = 0
# print(type, first_num, second_num)

if type is '+':
	result = plus(first_num, second_num)
elif type is '-':
	result = minus(first_num, second_num)
elif type is '*':
	result = multiple(first_num, second_num)
elif type is '/':
	result = divide(first_num, second_num)

print(result)