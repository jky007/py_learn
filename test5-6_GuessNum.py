#猜数字游戏，猜1~10的整数

def isEqual(num1,num2):
	if num1<num2:
		print ('too small')
		return False
	if num1>num2:
		print ('too big')
		return False
	if num1==num2:
		print ('bingo')
		return True
from random import randint
num = randint(1, 10)
print ('Guess what I think?')
bingo = False
while bingo == False:
	answer = eval(input())
	bingo = isEqual(answer, num)
