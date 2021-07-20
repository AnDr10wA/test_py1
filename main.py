from random import *

n = 15
random_list = []
for i in range(n):
    random_list.append(randint(1,9))
print(random_list)
print(set(random_list))
def count_number(number_list, number):
    numb = 0
    for i in number_list:
        if i == number:
            numb += 1
    print(numb)

    return numb
res = {}
for i in set(random_list):
    count = count_number(random_list, i)
    res[i] = count
    print(res)











