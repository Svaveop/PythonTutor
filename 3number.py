num = input("Enter number")
num1 = num[0]
num2 = num[1]
num3 = num[2]
if int(num) % 2 == 0:
    print(int(num1) * int(num2) * int(num2))
else:
    print(int(num1) + int(num2) + int(num2))
