user_input = int(input().strip())
absolute_value = 0;

if user_input >= 0:
	absolute_value = user_input
else:
	absolute_value = int(str(user_input).lstrip('-'))
	
print (absolute_value)