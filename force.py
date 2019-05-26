import matplotlib
import random
import networkx as nx
import matplotlib.pyplot as plt
import math
import time

from quadT import QuadTree,Rectangle

L=1
K_r=2
K_s=20
delta_t=0.1
N=20 #nodes counts
maxsqua=2

boundary=Rectangle(200,200,200,200)
qt=QuadTree(boundary,4)

class node:
    nodescount=0
    def __init__(self,x,y,neighbers):
        self.x=x
        self.y=y
        self.force_x=0
        self.force_y=0
        self.neighbers=neighbers
nodes=[]
t1=[0]*N
t2=[(0,0)]*N
fixed_pos =dict(zip(t1,t2)) #set fixed layout location

#initial values
for i in range(N):
    rx=random.uniform(0,25)
    ry=random.uniform(0,25)
    edges=random.randint(1,3) #randomly add edges 
    rn=[]
    for j in range(edges):
        rn.append(random.randint(0,N-1))
    nodes.append(node(rx,ry,rn))

    #QuadTree
    qt.insert(node(rx,ry,rn))
    
g = nx.Graph()
for i in range(N):
    for j in nodes[i].neighbers:
        g.add_edge(i,j)


def update_pos():
    #repulsion between all pairs
    for i in range(N-1):
        node1=nodes[i]
        for  j in range(i,N):
            node2=nodes[j]
            dx=node2.x-node1.x
            dy=node2.y-node1.y
            if dx!=0 or dy!=0:
                dissqua=dx*dx+dy*dy
                dis=math.sqrt(dissqua)
                force=K_r/dissqua
                fx=force*dx/dis
                fy=force*dy/dis
                nodes[i].force_x=node1.force_x-fx
                nodes[i].force_y=node1.force_y-fy
                nodes[j].force_x=node2.force_x+fx
                nodes[j].force_y=node2.force_y+fy

     #spring force between all neighbers
    for i in range(N-1):
        node1=nodes[i]
        for  j in node1.neighbers:
            node2=nodes[j]
            if i<j:
                dx=node2.x-node1.x
                dy=node2.y-node1.y
                if dx!=0 or dy!=0:
                    dissqua=dx*dx+dy*dy
                    dis=math.sqrt(dissqua)
                    force=K_s/(dis-L)
                    fx=force*dx/dis
                    fy=force*dy/dis
                    nodes[i].force_x=node1.force_x-fx
                    nodes[i].force_y=node1.force_y-fy
                    nodes[j].force_x=node2.force_x+fx
                    nodes[j].force_y=node2.force_y+fy
    #update positions
    for i in range(N):
        node=nodes[i]
        dx=delta_t*node.force_x
        dy=delta_t*node.force_y
        disp=dx*dx+dy*dy
        if disp>maxsqua:
            s=math.sqrt(maxsqua/disp)
            dx=dx*s
            dy=dy*s

        nodes[i].x=nodes[i].x+dx
        nodes[i].y=nodes[i].y+dy

        #print(i,nodes[i].x,nodes[i].y)

def showgraph(count):
    plt.subplot(231+count)
    plt.title(str(count*100)+" time(s)")
    #show the graph
    for i in range(N):
        fixed_pos[i]=(nodes[i].x,nodes[i].y)

    #pos=nx.spring_layout(g) # or you can use other layout set in the module
    nx.draw_networkx_nodes(g,pos = fixed_pos,node_color = 'g',node_size = 60)
    nx.draw_networkx_edges(g,pos = fixed_pos,edge_color='b')
    
    
#update counts
count=0
for i in range(600):
    update_pos()
    if i%100==0:
        showgraph(count)
        count+=1
plt.show()


 







