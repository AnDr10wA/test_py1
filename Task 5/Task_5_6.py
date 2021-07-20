from random import *


a = []
n = 20
for i in range(n):
    a.append(randint(1, 10))
print(a)
for i in a:
    if i > a[a.index(i) - 1]:
        print(a[: a.index(i)])