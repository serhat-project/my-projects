import random
from random import choice

name = (input('Please enter your full name : ').lower()).replace(' ','')
numbers = range(10)
num=str(random.choice(numbers))
chars = name + num
length = 8

print(''.join([choice(chars) for i in range(length)]))




