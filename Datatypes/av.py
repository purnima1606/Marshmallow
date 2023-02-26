# from  numpy improt random
#
import numpy as np
# arr = random.randint(40, size=(5))
# print(arr)

from random import random, seed, randint
l = []

# seed(9)
for i in range(10):
    value = randint(0,9)
    l.append(value)

print(l)

print(max(l))
print(min(l))

# **************************************************************************************************
"""   
arr = np.array([1,2,3])
b = np.array([4,5,6])

print('Array elements \n',arr)

print('Sum Of Array elements \n',arr.sum())

print('Sum Of Arr elements and b elements \n',arr + b)

"""
""" 
Array elements 
 [1 2 3]
Sum Of Array elements 
 6
Sum Of Arr elements and b elements 
 [5 7 9]

"""

#  *********************************************************************************************************
import re
s = "HeLLo PuRnImA"

a = re.findall(r'[A-Z]',s)
print(a)

b = re.findall(r'[a-z]', s)
print(b)

s1 ='abc abbc abcc aaabbc'

# c = re.findall(r'[^bc]',s1)
c = re.findall(r'[$bc]',s1)
print(c)

s2 = 'hell0 hii welcome'
# p = s2.split()
d = re.findall(r'[$me]',s2 )
print(d)
