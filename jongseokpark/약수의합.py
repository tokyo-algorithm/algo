# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())

result = user_input
for i in range(1, user_input):
    if (user_input % i) == 0:
        result += i

print(result)
