import random

import math
import time

class Node:
    
    def __init__(self,x,y):
        self.x=x
        self.y=y


class Rectangle:
    
    def __init__(self,x,y,w,h):
        self.x=x
        self.y=y
        self.w=w
        self.h=h

    def contains(self,Node):
        return (Node.x>=(self.x-self.w) 
                and Node.x<=(self.x+self.w)
                and Node.y>=(self.y-self.h)
                and Node.y<=(self.y+self.h))



class QuadTree:
    
    def __init__(self,boundary,n):
        self.boundary=boundary
        self.capacity=n
        self.nodes=[]
        self.divided=False

    def subdivide(self):
        #print('do subdivide')
        x=self.boundary.x
        y=self.boundary.y
        w=self.boundary.w
        h=self.boundary.h

        ne=Rectangle(x+w/2,y+h/2,w/2,h/2)
        self.northeast=QuadTree(ne,self.capacity)
        nw=Rectangle(x-w/2,y+h/2,w/2,h/2)
        self.northwest=QuadTree(nw,self.capacity)
        se=Rectangle(x+w/2,y-h/2,w/2,h/2)
        self.southeast=QuadTree(se,self.capacity)
        sw=Rectangle(x-w/2,y-h/2,w/2,h/2)
        self.southwest=QuadTree(sw,self.capacity)
        self.divided=True

    def insert(self,Node):
        if not self.boundary.contains(Node):
            return

        if len(self.nodes)<self.capacity:
            self.nodes.append(Node)
        else:
            if(not self.divided):
                self.subdivide()
    
            self.northeast.insert(Node)
            self.northwest.insert(Node)
            self.southeast.insert(Node)
            self.southwest.insert(Node)

    

    def print(self,layer):
        #print(len(self.nodes))
        for node in self.nodes:
            print(node.x,node.y)
        newlayer=layer+1
        print('\n')
        if(self.divided):
            print(str(layer)+'-northeast')
            self.northeast.print(newlayer)
            print(str(layer)+'-northwest')
            self.northwest.print(newlayer)
            print(str(layer)+"-southeast")
            self.southeast.print(newlayer) 
            print(str(layer)+"-southwest")
            self.southwest.print(newlayer)

# b=Rectangle(200,200,200,200)
# q=QuadTree(b,4)
# for i in range(20):
#     rx=round(random.uniform(0,400),2)
#     ry=round(random.uniform(0,400),2)
#     p=Node(rx,ry)
#     q.insert(p)

# q.print(layer=1)