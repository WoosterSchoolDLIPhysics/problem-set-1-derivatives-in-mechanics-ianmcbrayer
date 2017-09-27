#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 11:39:58 2017

@author: apple
"""
from pylab import *

x = 3*sin(2*pi*t)
y = 2*cos(2*pi*t)
vx = 6*pi*cos(2*pi*t)/5
vy = -4*pi*sin(2*pi*t)/5
ax = -12*pi**2*sin(2*pi*t)/5
ay = -8*pi**2*cos(2*pi*t)/5

t = linspace(0,1,100)

figure(1)

for it in arange(len(t)):
    clf()
    #subplot(131)
    plot(x,y,color='red')
    plot([0,x[it]],[0,y[it]],'r-*')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*x[it],1.2*y[it],r'$\vec{x}$',color='black',size=15)

    
    plot(vx,vy,color='green')
    plot([0,vx[it]],[0,vy[it]],'g-*')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*vx[it],1.2*vy[it],r'$\vec{v}$',color='black',size=15)
    
    plot(ax,ay,color='blue')
    plot([0,ax[it]],[0,ay[it]],'b-*')
    axis('equal'); xlabel(r'$x$'); ylabel(r'$y$')
    text(1.2*ax[it],1.2*ay[it],r'$\vec{a}$',color='black',size=15)

    #text(1.1*x[it]/10,1.1*y[it]/10,r'$\vec{a}$',color='red',size=15)
    grid()
    #savefig('frame_%03d.png' % it)

    pause(.001)