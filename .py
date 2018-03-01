# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:15:36 2018

@author: Ricardo
"""
import numpy


def digitroot(a):
    y = len(a)
    h = []
    maxval =[]
    for x in range(y):
        b = a[x]
        g = len(str(b))
        counter = 0 
        for j in range (len(str(b))):
            alph = str(b)
            counter = counter + int(alph[j])
        h.append(counter)
    jimmy =sorted(h, key=int, reverse=True)
    for x in range(len(a)):
        if x < len(jimmy):
            c = h.index(jimmy[x])
            maxval.append(a[c])
            jimmy.remove(jimmy[x])
        else break :
    return maxval    
