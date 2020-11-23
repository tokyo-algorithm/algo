user_input = int(input())
for i in range(1, user_input+1):
	if i % 3 is 0:
		print('X', end=' ')
	else:
		print(i, end=' ')