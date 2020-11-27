# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

num = int(input())
i = 1
j = 1

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i * j, end=" ")
        if j % num is 0:
            print()
