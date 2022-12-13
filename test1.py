import turtle

t = turtle.
print("1. forward")
print("2. backward")
print("3. right")
print("4. left")


turtle.forward()
turtle.right()
turtle.left()
turtle.backward()


choose = int(input("Choose options: "))
if choose == 1:
	print("forward")
elif choose == 2:
 	print("backward")
elif choose == 3:
 	print("right")
elif choose == 4:
 	print("left")

turtle.mainloop()






