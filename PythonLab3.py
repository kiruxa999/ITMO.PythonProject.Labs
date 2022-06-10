import math

from statistics import mean
from statistics import median
from statistics import stdev

from random import randint

list1 = [1,2,3,4,5,6,7,8,9,0]
print(math.fsum(list1))
print(mean(list1))
print(median(list1))
print(stdev(list1))

x = randint(1, 100)
print(x)