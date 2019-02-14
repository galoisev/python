# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 19:55:54 2019

@author: paulune
"""


import os
import numpy as np
import scipy as sp


'''
IN : A, Matrice sysmetrique definie positive
IN : b, vecteur
OUT: x, vecteur 
'''
def  GradConj(x,A,b):    
    x0 = x    
    r0 = b - np.dot(A,x0)
    p0 = r0
    alpha1 = np.vdot(r0,r0)/np.vdot(p0,np.dot(A,p0))
    x1 = x0 + alpha1*p0
    r1 = r0 - alpha1*np.dot(A,p0)
    beta1 = np.vdot(r1,r1)/np.vdot(r0,r0)
    p1 = r1 + beta1*p0    
    return x1




    
def  GC(x,A,b):    
    x0 = x
    r0 = b-A*x0
    ite = 0
    delta = 1e3
    while(delta > 1.e-3):
        p0 = r0
        alpha1 = np.dot(r0,r0)/np.dot(p0,A*p0)
        x1 = x0 + alpha1*p0
        r1 = r0 - alpha1*A*p0
        beta1 = np.dot(r1,r1)/np.dot(r0,r0)
        p1 = r1 + beta1*p0
         #delta = np.dot((x1-x0),(x1-x0))
        if(ite > 1000):
            break
        ite = ite+1
        p0 = p1
        r0 = r1
        x0 = x1
    x = x0
    return x
