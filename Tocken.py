number = input("Enter number")
num1 = number[0]
num2 = number[1]
num3 = number[2]
num4 = number[3]
num5 = number[4]
num6 = number[5]
summa1 = int(num1) + int(num2) + int(num3)
summa2 = int(num2) + int(num5) + int(num6)
if summa1 == summa2:
    print("lucky")
else:
    print("unlucky")
