# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# user_input = input()
# 2 4 5 8 -9 11 -15 17 18 
# 18 -15 11 -9 8 땡
user_input = ['8', '11', '-9', '2', '5', '18', '17', '-15', '4']
positive_number = []
negative_number = []

for value in user_input:
  value = int(value)
  if value > 0:
    positive_number.append(value)
  else:
    negative_number.append(value)
# [18, 17, 11, 8, 5, 4, 2]
positive_number = sorted(positive_number, reverse=True)
# [-15, -9]
negative_number = sorted(negative_number)
print(positive_number)
print(negative_number)

started_with_positive_number = 0
container = []
if abs(positive_number[0]) > abs(negative_number[0]):
  started_with_positive_number = 1

if started_with_positive_number > 0:
  container.append(positive_number[0])
else:
  container.append(negative_number[0])

# 양수 먼저 시작
for i in negative_number:
  if(abs(container[len(container) - 1]) > abs(i)):
    container.append(i)
    break

for i in positive_number:
  if(abs(container[len(container) - 1]) > abs(i)):
    container.append(i)
    break

for i in negative_number:
  if(abs(container[len(container) - 1]) > abs(i)):
    container.append(i)
    break

for i in positive_number:
  if(abs(container[len(container) - 1]) > abs(i)):
    container.append(i)
    break

for i in negative_number:
  if(abs(container[len(container) - 1]) > abs(i)):
    container.append(i)
    break

for i in positive_number:
  if(abs(container[len(container) - 1]) > abs(i)):
    container.append(i)
    break

print(container)

# 컨테이너 정보는 0이 아닌 정수로 표현된다.
# 두 가지 색상을 층마다 교차로 칠하는 방식
# 정수의 값이 음수면 흰색 / 양수명 검은색
# 컨테이너의 크기는 정수의 절대값
# 컨테이너는 모두 다른 크기
# 최대한 높은 건물
# 위층의 컨테이너는 아래층보다 작음

