print("1 - Задача 1 ")
print("2 - Задача 2 ")
print("3 - Задача 3 ")
print("4 - Задача 4 ")
k=int(input("Введите номер задачи: "))
if k==1:
	a=int(input("Введите А: "))
	b=int(input("Введите В: "))
	print("A + B = ",a+b)
elif k==2:
	a=int(input("Введите А: "))
	b=int(input("Введите В: "))
	print("A - B = ",a-b)
if k==3:
	a=int(input("Введите А: "))
	b=int(input("Введите В: "))
	print("A * B = ",a*b)
if k==4:
	a=int(input("Введите А: "))
	b=int(input("Введите В: "))
	print("A / B = ",a/b)
else:
	print("Неверный номер задачи")



