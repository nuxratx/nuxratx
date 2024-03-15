#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:19:19 2024

@author: nuxratx
""" 



import math 
from turtle import *
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-22*\
    math.cos(3*k)-\
    math.cos(4*k)
speed(90000)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20,heartb(i)*20)
    for j in range (5):
        color("red")
    goto(0,0)
done()
    
    
