#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from tkinter import *
get_ipython().run_line_magic('matplotlib', 'qt')


# In[3]:


def normalize_complex(number):
    return number / abs(number)

class fractal:
    def __init__(self, geom):
        self.geom = geom
        self.length = abs(self.geom[-1] - self.geom[0])
        self.norm = normalize_complex(self.geom[-1] - self.geom[0])

        self.line_1 = self.geom
        self.line_2 = []
        self.line_3 = []
        self.line_4 = []
        self.line_5 = []

        for i in range(len(self.geom) - 1):
            self.part = self.geom[i] + self.geom / self.norm * (self.geom[i + 1] - self.geom[i]) / self.length 
            for self.comp in self.part:
                self.line_2.append(self.comp)
            for n in range(len(self.part) - 1):
                self.part2 = self.part[n] + self.geom / self.norm * (self.part[n + 1] - self.part[n]) / self.length
                for self.comp in self.part2:
                    self.line_3.append(self.comp)
                for f in range(len(self.part2) - 1):
                    self.part3 = self.part2[f] + self.geom / self.norm * (self.part2[f + 1] - self.part2[f]) / self.length
                    for self.comp in self.part3:
                        self.line_4.append(self.comp)
                    for g in range(len(self.part3) - 1):
                        self.part4 = self.part3[g] + self.geom / self.norm * (self.part3[g + 1] - self.part3[g]) / self.length
                        for self.comp in self.part4:
                            self.line_5.append(self.comp)

    def plot_fractal(self, level):
        plt.figure()
    #     plt.xlim([0 - location_x, length - location_x])
        if level == 1:
            plt.plot(np.real(self.line_1), np.imag(self.line_1), c='k')
        elif level == 2:
            plt.plot(np.real(self.line_2), np.imag(self.line_2), c='k')
        elif level == 3:
            plt.plot(np.real(self.line_3), np.imag(self.line_3), c='k')
        elif level == 4:
            plt.plot(np.real(self.line_4), np.imag(self.line_4), c='k')
        elif level == 5:
            plt.plot(np.real(self.line_5), np.imag(self.line_5), c='k')
            
        

canvas_width = 800
canvas_height = 800



X = []
Y = []


def draw( event ):
    global X
    global Y
    if not X:
        X.append( event.x )
        Y.append( event.y )
 
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        w.create_oval(x1, y1, x2, y2, tags = 'original')

    else:

        X.append( event.x )
        Y.append( event.y )
        w.create_line( X[-1], Y[-1], X[-2], Y[-2], tags = 'original')
        
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        w.create_oval(x1, y1, x2, y2, tags = 'original')
        
        create()

        


def create():
    delete('line')
    
    x = np.asarray(X) - X[0] 
    y = np.asarray(Y) - Y[0]
    geom = x + y*1.j
    frac = fractal(geom)
    for item in range(len(frac.line_2) - 1):
        w.create_line(np.real(frac.line_2[item]) + canvas_width /2. + canvas_width /20., 
                      np.imag(frac.line_2[item]) + Y[0], 
                      np.real(frac.line_2[item+1]) + canvas_width /2. + canvas_width /20., 
                      np.imag(frac.line_2[item+1]) + Y[0],
                      tags='line') 
        
    for item in range(len(frac.line_3) - 1):
        w.create_line(np.real(frac.line_3[item]) + canvas_width /10., 
                      np.imag(frac.line_3[item]) + canvas_height *3/4., 
                      np.real(frac.line_3[item+1]) + canvas_width /10., 
                      np.imag(frac.line_3[item+1]) + canvas_height *3/4.,
                      tags='line')
        
    for item in range(len(frac.line_4) - 1):
        w.create_line(np.real(frac.line_4[item]) + canvas_width /2. + canvas_width /20., 
                      np.imag(frac.line_4[item]) + canvas_height *3/4., 
                      np.real(frac.line_4[item+1]) + canvas_width /2. + canvas_width /20., 
                      np.imag(frac.line_4[item+1]) + canvas_height *3/4.,
                      tags='line')

        
def delete(x):
    w.delete(x)

    
def restart():
    global X
    global Y
    X = []
    Y = []
    w.delete('line')
    w.delete('original')


   
    
master = Tk()
master.title( "Draw Fractal" )
w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack(expand = YES, fill = BOTH)
w.bind('<ButtonPress-1>', draw)


B = Button(master, text ="Restart", command = restart)
B.pack()



w.create_rectangle(canvas_width/20., 
                   canvas_height/20., 
                   canvas_width/2. - canvas_width/20., 
                   canvas_height/2. - canvas_height/20.) 

w.create_text(canvas_width/4., 
              canvas_height/2., 
              text = 'Draw here, or not...') 

    
mainloop()


# In[ ]:




