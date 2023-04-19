### Introduction

This project provides a program generating the Sapinski triangle, a _fractal_.

### The Sapinski triangle
The way it is obtained is of particular interest: 
1. start by drawing 3 points, the vertices of 
a triangle 
2. draw a 4th point wherever you want (better on the inner surface of the triangle) 
3. randomly chose a vertex and draw a point exactly at half distance between the last point 
drawn and the vertex chosen 
4. repeat the operation as much time as you want and you'll always obtain the fractal image

### Project info
>**main.py**

This file contains the main program. 
You can choose the _starting point_ and the number of _total points_ drown by editing 
the attributes `start_pt` and `total_pt`. 

>**colors.py**

This file contains a _dictionary_ and a _list_ with 9 colors.   

### Required Modules
The program makes use of the module `Pillow`