# 1. 결과: 실패 원인: 배열 출력시 [ ] 모양이 나오고, overflow 가 한번에 출력이 안되고 바로 출력이 됨.
input_num = int(input())
arr = []
for i in range(input_num):
	num = int(input())
	if(num == 0):
		if(len(arr) > 10):
			print("overflow")
		else:
			num1 = int(input())
			arr.append(num1)
	elif(num == 1):
		if(len(arr) < 1):
			print("underflow")
		else:
			arr.pop()
	else:
		break

print(arr)