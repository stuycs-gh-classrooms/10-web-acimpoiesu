#!/usr/bin/python
print('Content-type: text/html\n')

from random import random
def randomy():
    return random()
print("your number is:")
print(randomy())