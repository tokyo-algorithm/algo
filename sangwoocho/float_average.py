# 시험성적 평균과 등급 구하기

# 입력 3개 받아서 공백을 기준으로 나눠서 실수로 바꾸고 변수에 할당
kor, eng, math = map(float, input().split())


# 소숫점 2자리까지 판별 함수 round(n,2) **2자리까지round() 함수는 끝자리가 0이면 출력을 하지 않는 문제가 있습니다.
average_score = round((kor + eng + math) / 3, 2)

# format이 좋음 반올림을 하는 round() 함수를 내장하고 있습니다.


if average_score >= 90:
    print(format(average_score, '.2f'), "A")
elif average_score >= 80:
    print(format(average_score, '.2f'), "B")
elif average_score >= 70:
    print(format(average_score, '.2f'), "C")
elif average_score >= 60:
    print(format(average_score, '.2f'), "D")
else:
    print(format(average_score, '.2f'), "F")
