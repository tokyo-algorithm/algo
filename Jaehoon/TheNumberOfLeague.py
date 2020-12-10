print("The Start of cal")
n= int(input("Input the number of team:"))
def cal():
	print("The number of team is", n )
print("The End of cal")
	
print("The Start of main")
def main():
	j = 0
	k = 0
	while j < n:
	  k = k + j
	  j = j + 1
	  print ("The number of game is", k)	
print("The End of main")

if __name__ == '__main__':
   cal()
   main()
print("The end")