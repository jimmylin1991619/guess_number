#讓使用者重複輸入數字去猜
#猜對的話 印出"終於猜對了!"
#猜錯的話要告訴他 比答案大/小

import random #載入random模組
start = input('請輸入起始範圍: ')
end = input('請輸入結束範圍: ')
r = random.randint(int(start), int(end))
count = 0
while True:
	count = count + 1
	guess = input('請猜猜數字: ')
	guess = int(guess)
	if r == guess:
		print('終於猜對了!') 
		print('這是你猜的第', count, '次')
		break
	else:
		if r != guess and r > guess:
			print('比答案小')  
		else:
			print('比答案大')
	print('這是你猜的第', count, '次')






 	