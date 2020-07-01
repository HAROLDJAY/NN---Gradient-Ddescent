# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:20:08 2020

@author: hp
"""


import random
def function(x, y):
    return 8*x + 12*y + 20

x = [random.random() for _ in range(150)]
y = [random.random() for _ in range(150)]
z = [function(x_, y_) for x_, y_ in zip(x, y)]
data = list (zip(x, y, z))
data[0:150]
m1 = random.random()
m2 = random.random()
b = random.random()
lr = 0.001
def get_answer(x,y):
    return m1 * x + m2 * y + b
x_, y_, z_ = data[0]
print(get_answer(x_, y_), z_)
def get_error(x, y, z):
    P = get_answer(x, y)
    error = (P - z)**2
    return error
    get_error(x_, y_, z_)
    
def update_values(x, y, z):
    global m1, m2, b
    factor = 2 * (get_answer(x, y) - z)
    dm1 = factor * x
    dm2 = factor * y
    db = factor
    
    m1 = m1 - dm1 * lr
    m2 = m2 - dm2 * lr
    b = b - db * lr
    
for _ in range(100):
    for x_, y_, z_ in data:
        print(x_, y_, z_)
        print('\tPrediction: ', get_answer(x_, y_))
        print('\tError: ', get_error(x_, y_, z_))
        update_values(x_, y_, z_)
        
    