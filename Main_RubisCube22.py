# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 18:19:02 2024

@author: Mounir

# Inspired from : https://github.com/CiSienx/Rubic-s-cube

"""

from vpython import *
import numpy as np
import random

####################################################################################
####################     Construction du Cube 2x2 par face   #######################
####################################################################################

# tiles is a structure that group all the tiles of the rubiscube ; 24 in total
tiles = []
# dA is the step used for the rotation
dA = np.pi/4
## Creation of a Sphere centered and having a radius of 1 with a black color
sphere(pos=vector(0,0,0),size=vector(2,2,2),color=vector(0,0,0))
## creation of vectors which will be used to draw the squares of each face 
tile_pos = [    
            [vector(-0.5, 0.5, 1),vector(0.5, 0.5, 1),           #Front high   Blue
             vector(-0.5, -0.5, 1),vector(0.5, -0.5, 1),         #Front low                         
             ],
            [vector(-1, 0.5, -0.5),vector(-1, 0.5, 0.5),         #Left high   Yellow
             vector(-1, -0.5, -0.5),vector(-1, -0.5, 0.5),       #Left low                          
             ],
            [vector(0.5, 0.5, -1),vector(-0.5, 0.5, -1),         #Back high   Green
             vector(0.5, -0.5, -1),vector(-0.5, -0.5, -1),       #Back low                          
             ],
            [vector(1, 0.5, -0.5),vector(1, 0.5, 0.5),           #Right high  White
             vector(1, -0.5, -0.5),vector(1, -0.5, 0.5),         #Right low                          
             ],          
            [vector(0.5, -1, 0.5),vector(-0.5, -1, 0.5),         #Bottom high  Orange
             vector(0.5, -1, -0.5),vector(-0.5, -1, -0.5),       #Bottom low                          
             ],                              
            [vector(0.5, 1, -0.5),vector(-0.5, 1, -0.5),         #Top high    Red
             vector(0.5, 1, 0.5),vector(-0.5, 1, 0.5),           #Top low                          
             ],     
            ]
## Define a color for each face 
colors = [color.blue,color.yellow,color.green,color.white,color.orange,color.red]
## Angles to be used to rotate the squares to match the righ face of Rubis Cube
angle = [(0,vector(0,0,0)),(np.pi/2,vector(0,1,0)),(0,vector(0,0,0)),(np.pi/2,vector(0,1,0)),(np.pi/2,vector(1,0,0)),(np.pi/2,vector(1,0,0))]
# Draw the squares based on the information above and using the box function from vPython
for rank,side in enumerate(tile_pos):
    for vec in side:
        tile = box(pos=vec,size=vector(0.99,0.99,0.1),color=colors[rank])
        tile.rotate(angle = angle[rank][0],axis=angle[rank][1])
        tiles.append(tile)


####################################################################################
####################     Basic animation . 1 Flip Top Right  #######################
####################################################################################

positions = {'front': [], 'left': [], 'back': [], 'right': [], 'bottom': [], 'top': []}
positions['front']  = tiles[0:4]
positions['left']   = tiles[4:8]
positions['back']   = tiles[8:12]
positions['right']  = tiles[12:16]
positions['bottom'] = tiles[16:20]
positions['top']    = tiles[20:24]

pieces = positions['front']
for tile in pieces:
    tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))

pieces = positions['top']
for tile in pieces:
    tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))
    
   







