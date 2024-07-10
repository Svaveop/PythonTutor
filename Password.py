import random
import string

z = (random.randint(1, 9))
a = (random.randint(0, 9))
b = (random.randint(0, 9))
c = (random.randint(0, 9))
d = (random.randint(0, 9))
e = (random.randint(0, 9))
f = (random.randint(0, 9))
g = (random.randint(0, 9))
print(str(z) + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g))

print("or")

password_1 = ""
password_2 = ""
for i in range(8):
    a = random.randint(0, 9)
    password_1 += str(a)
    password_2 += random.choice(string.ascii_letters + string.digits)
print(password_1)
print(password_2)
