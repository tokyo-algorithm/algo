# 피라미드
# 층 수에 맞는 피라미드 출력
# 문제 접근 방법,
# 결과값을 먼저 생각하고, 변수를 두개로 나눔( 별, 띄어쓰기)
# 별은 홀수로 매번 루프마다 나타남
# 띄어쓰기는 매번 루프마다 전체 층수에서 순회하는 인덱스마다 줄어들음
user_input = int(input())


for i in range(1, user_input + 1):

    # 별은 홀수로 증가함,
    star = 2*i - 1
    # 띄어쓰기는 전체 층 기준으로 1씩 줄어들음,
    spacing = user_input - i

    result = spacing * " " + star * "*"
    print(result)
