# # sum = 0
# # for i in range(1,50):
# # 	sum = sum + i
# # 	print(i)

# oddSum = 0
# for i in range(50):
# 	oddSum = oddSum + i 
# 	print(oddSum)


n = int(input("number:  "))

if n % 3 == 0:
	print ("Divisible by 3")
elif n % 4 == 0:
	print ("Divisible by 4")
elif n % 3 != 0 and n % 4 != 0:
	print ("Not divisible by 3 or 4")
