# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 13:49:57 2015

@author: Piotr Skorupa
"""

from visual import *
text(text='SPADEK KULI',
    depth=-0.3, color=color.green, pos=(3,10,0))
podloga = box (pos=(-3,0,0), length=2, height=20, width=2, color=color.blue)
pilka = sphere (pos=(0,10,0), radius=1, color=color.green)
pilka.velocity = vector(0,-1,0)
dt = 0.01
podloga2 = box (pos=(0,-10,0), length=4, height=1, width=2, color=color.blue)

while 1:
   rate (100)
   pilka.pos = pilka.pos + pilka.velocity*dt
   if pilka.y < -8.9:
       pilka.velocity.y = 0
       pilka.pos.y = 10
   else:
       pilka.velocity.y = pilka.velocity.y - 9.8*dt
    
   
