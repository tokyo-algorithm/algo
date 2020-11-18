# 약수 구하기
user_input = int(input())
# 리스트에 결과를 담음, 리스트는 루프 밖에 있어야함, 루프 안에있으면 필요없음
# 출력함수는 end 매개변수로 디폴트는 \n임

for i in range(1, user_input + 1):

    if user_input % i == 0:
        print(i, end=' ')
