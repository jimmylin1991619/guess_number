#讓使用者重複輸入數字去猜
#猜對的話 印出"終於猜對了!"
#猜錯的話要告訴他 比答案大/小

import random #載入random模組
r = random.randint(1, 100) #隨機正整數 random int = randint(start, end)
#print(r)

while True:
	guess = input('請猜猜數字: ')
	guess = int(guess)
	if r == guess:
		print('終於猜對了!') 
		break
	else:
		if r != guess and r > guess:
			print('比答案小')  
		else:
			print('比答案大')







 	