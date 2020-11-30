#https://level.goorm.io/exam/43171/%EC%96%B4%EB%8A%90-%EA%B0%9C%EB%B0%9C%EC%9E%90-%EC%9D%B4%EC%95%BC%EA%B8%B0/quiz/1

# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = input()
curNums =list(user_input)
curNums = list(map(int, curNums))
curMax = max(curNums)


#helper fn
def is_square(i: int) -> bool:
		#code splitting here
		import math
    sqrt = math.sqrt(i)
    return (sqrt - int(sqrt)) == 0
	
	
#limit to 1000 for the overflow
for i in range(curMax+1, 1000):
	curSum = 0
	for index in range(len(curNums)):
		#actual logic to add up all the numbers
		curSum += curNums[len(curNums)-1 - index] * (i ** index)
	#check the square
	if is_square(curSum):
		print(i)
		break
