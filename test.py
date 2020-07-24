'''
Created on 24-Jul-2020

@author: kailash
'''


a1 = 10
print(type(a1))
print("divison is",  a1/1.2)

# strings

b = "My name is Python"
print(len(b)) 
c = b.replace('name', 'a', 1)
c = b.split(' ')
print (c)

# Tuple -> immutable
tup = (1, 'sss', 3.14)
tup_int = (1,2,3)
print(max(tup_int)) 
print(tup[1])

if 3 in tup_int:
    print('3 is present in tuple')

# list -> mutable, reverse, insert, sort, l1 + l2, L1*3 + l2
# dictionary -> mutable, unordered collection, d1.keys(), d1.values(), d1.pop("key")
# Set ->    unordered, unindexed collection, unique elements, add(), update([1,2,3]), 
#           remove("1"), union(), intersection

# lambda
lam = lambda x: x*x*x
print (lam(10))

list1 = [1,3,4,8,9]
list_odd = list(filter(lambda x: (x%2!=0), list1))
print(list_odd)

list_task_mul_2 = list(map(lambda x : x*2,list1)) 
print(list_task_mul_2)

from functools import reduce # reducedto consolidated value
sum_list = reduce(lambda x,y: x+y, list1)
print(sum_list)

# Inheritance -> multiple, multilevel

class Phone_base:
    def __init__(self, color):
        self.color  = color

class Phone(Phone_base):
    def __init__(self,color, brand):
        super().__init__(color)
        self.brand = brand
        
    def set_color(self, color):
        self.color = color
        
    def get_color (self):
        return self.color
    
phone_moto = Phone("Red", "mi");
phone_moto.set_color("blue")
print(phone_moto.get_color())

# numpy -> shape, random.randint, vstack, hstack, column_stack(), 
#        intersect1d, setdiff1d (difference), 
#        sum([n1,n2]), sum([n1,n2], axis = 0) for columns sum 
#        n1 = n1+1, n1=n1-1, n1=n1*2, n1=n1/2,
#        mean, median, std (standard deviation), save(), load()
import numpy as np

np_z = np.zeros((10,10))
np_z = np.full((10,10), 10)
np_z = np.arange(10,20, 5) # [10,15]
print(np_z)

# pandas -> panel data, data manipulation
import pandas as pd

pd1 = pd.Series([0,19,27,'a'])
print(pd1)