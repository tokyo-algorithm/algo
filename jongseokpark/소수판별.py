# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())


# 소수 == 1과 자신을 제외하고는 나눌 수 없는 수
def prime_number():
    if user_input == 1:
        print("True")
        return
    # 짝수는 소수가 아니다.
    elif (user_input % 2) == 0:
        print("False")
        return
    # 홀수중 소수가 아닐경우
    for i in range(3, user_input, 2):
        if user_input % i == 0:
            print("False")
            return
    print("True")


prime_number()
