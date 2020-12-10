# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()


def calculate():
    split_user_input = user_input.split(" ")
    first_number = int(split_user_input[0])
    operator = split_user_input[1]
    second_number = int(split_user_input[2])
    if operator == "+":
        print(first_number + second_number)
        return
    elif operator == "-":
        print(first_number - second_number)
        return
    elif operator == "*":
        print(first_number * second_number)
        return
    elif operator == "/":
        # print(format(first_number / second_number, ".2f"))
        print("%(result).2f" % {'result': first_number / second_number})



calculate()
