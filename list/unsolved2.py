#Write a Python program to change the position of every n-th value with the (n+1)th in a list

from itertools import zip_longest, chain, tee
def replace(list):
    list1, list2 = tee(iter(list), 2)
    return list(chain.from_iterable(zip_longest(list[1::2], list[::2])))
n = [0,12,22,34,45,50]
print(replace(n))