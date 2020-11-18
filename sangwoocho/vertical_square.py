# 세로 순서 사각형
"""
정수 리스트 => 공백이 포함된 문자열(숫자를 문자로 가진) 리스트
numbers = [3, 30, 34, 5, 9]
print(' '.join(str(e) for e in numbers))

"""

size = int(input())


for i in range(1, size+1):
    arr = []
    sum = 0
    for j in range(size):
        arr.append(i + sum)
        sum = sum + size

    print(' '.join(str(e) for e in arr) + " ")
