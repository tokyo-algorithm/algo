# 최소값 문제

# 인풋을 두개 받고, 두번째 인풋에서 첫번쨰 인풋의 길이만큼만 나타내서 배열만든후 최소값씀

"""
Go도 그렇고 Erlang 같은 고전 언어에서도 그렇고 '_'의 의미는 굳이 어떤 변수에 값을 할당해서 쓰지 않을 경우에 사용하는 syntax 입니다. 예제 소스코드로 보면 리스트의 요소 개수만큼 이터레이션은 하지만 요소를 가져다가 쓰지 않기 때문에 굳이 변수를 사용하지 않고 _로 요소값을 버린다고 생각하시면 쉬울거 같네요.

python에서는 ' throwaway variable' 라고 보통 부릅니다. 관련링크: http://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
"""
first_input = int(input())
# map(변환 함수, 순회 가능한 데이터)
#  input().split()
# 디폴트로 split (" ")와 같음.
# https://m.blog.naver.com/ygj01069/221944161510

second_input = list(map(int, input().split(" ", first_input)[:first_input]))

# Limiting number of input values in an array/list in Python
# 최대 split을 정의하고 나머지부분은 자른후에 배열로 만듦
# https://www.programiz.com/python-programming/methods/string/split

print(min(second_input))
