#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 14:59:41 2024

@author: nusratalam
"""

import turtle

anms = turtle.Turtle()
anms.color("purple", "yellow")
anms.speed(300)
anms.fd(-160)

anms.begin_fill()

for i in range(90):
    anms.forward(300)
    anms.left(170)

anms.end_fill()

turtle.mainloop()