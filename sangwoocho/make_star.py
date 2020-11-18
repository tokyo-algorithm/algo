# 모양찍기
# -1씩 줄어드는 등차수열의 각 항만큼 별로 표시
user_input = int(input())

for i in range(user_input, 0, -1):
    result = i * '*'
    print(result)
