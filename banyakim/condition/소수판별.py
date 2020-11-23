num = int(input())
divisor_list = []
answer = ''

for i in range(1, num + 1):
	if num % i == 0:
		divisor_list.append(i)
if len(divisor_list) == 2:
	answer = 'True'
else:
	answer = 'False'
print(answer)