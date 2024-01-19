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

######################################################################################
####################     Create a list associating the tiles   #######################
######################################################################################

positions = {'front_top': [], 'front_bottom': [], 'back': [], 'right': [], 'bottom': [], 'top': []}

positions['front_top']     = (tiles[0],tiles[1])
positions['front_bottom']  = (tiles[2],tiles[3])
positions['front_left']    = (tiles[0],tiles[2])
positions['front_right']   = (tiles[1],tiles[3])

positions['left_top']     = (tiles[4],tiles[5])
positions['left_bottom']  = (tiles[6],tiles[7])
positions['left_left']    = (tiles[4],tiles[6])
positions['left_right']   = (tiles[5],tiles[7])

positions['back_top']     = (tiles[8],tiles[9])
positions['back_bottom']  = (tiles[10],tiles[11])
positions['back_left']    = (tiles[8],tiles[10])
positions['back_right']   = (tiles[9],tiles[11])

positions['right_top']     = (tiles[12],tiles[13])
positions['right_bottom']  = (tiles[14],tiles[15])
positions['right_right']    = (tiles[12],tiles[14])
positions['right_left']   = (tiles[13],tiles[15])

positions['bottom_top']     = (tiles[16],tiles[17])
positions['bottom_bottom']  = (tiles[18],tiles[19])
positions['bottom_right']    = (tiles[16],tiles[18])
positions['bottom_left']   = (tiles[17],tiles[19])

positions['top_top']     = (tiles[20],tiles[21])
positions['top_bottom']  = (tiles[22],tiles[23])
positions['top_right']    = (tiles[20],tiles[22])
positions['top_left']   = (tiles[21],tiles[23])


######################################################################################
#################     f rotation : front rotation anti clockwise   ##################
######################################################################################
# dA is the step used for the rotation
def f():
    dA = -np.pi/50
    DA = dA
    while DA > -np.pi/2 -np.pi/50 :
        DA = DA - np.pi/50 
        pieces = positions['front_top']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))    
        pieces = positions['front_bottom']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))    
        pieces = positions['top_bottom']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['bottom_top']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['left_right']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['right_left']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))
        rate(30)

######################################################################################
#################     f' rotation : front rotation anti clockwise   ##################
######################################################################################
# dA is the step used for the rotation
def f_prime():
    dA = np.pi/50
    DA = dA
    while DA < np.pi/2 + np.pi/50 :
        DA = DA + np.pi/50 
        pieces = positions['front_top']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))    
        pieces = positions['front_bottom']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))    
        pieces = positions['top_bottom']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['bottom_top']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['left_right']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['right_left']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))
        rate(30)
        
    
######################################################################################
#################     b rotation : back rotation anti clockwise   ##################
######################################################################################
# dA is the step used for the rotation
def b():
    dA = -np.pi/50
    DA = dA
    while DA > -np.pi/2 -np.pi/50 :
        DA = DA - np.pi/50 
        pieces = positions['back_top']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))    
        pieces = positions['back_bottom']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))    
        pieces = positions['top_top']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['bottom_bottom']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['left_left']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['right_right']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))
        rate(30)
 
    
######################################################################################
#################     b_prime rotation : back rotation  clockwise   ##################
######################################################################################
# dA is the step used for the rotation
def b_prime():
     dA = np.pi/50
     DA = dA
     while DA < np.pi/2 + np.pi/50 :
        DA = DA + np.pi/50 
        pieces = positions['back_top']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))    
        pieces = positions['back_bottom']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))    
        pieces = positions['top_top']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['bottom_bottom']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['left_left']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))        
        pieces = positions['right_right']
        for tile in pieces:
            tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))
        rate(30)    
    
    
# input("f_prime ?")    
# f_prime()    
    
    
# pieces = positions['front_bottom']
# for tile in pieces:
#     tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))
# pieces = positions['top_bottom']
# for tile in pieces:
#     tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))




# pieces = positions['top']
# for tile in pieces:
#     tile.rotate(angle= dA,axis = vector(0,0,1),origin=vector(0,0,0))
    
   







