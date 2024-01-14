# TITLE: Segmentation Class for Software Assignment #2
# CLASS: CSCI 332, Fall 2023
# Author: Aspen Morgan
# Date: 2023.12.13
# Collaborated (conceptually) with Jayce Holdsambeck

import numpy as np

class segmentationClass:
    # class initializer
    def __init__(self):
        self = self

    # x_a is the coordinates of one foreground pixel
    def x_a(self, x_a):
        self.x_a = x_a

    # x_b is the coordinates of one background pixel
    def x_b(self, x_b) :
        self.x_b = x_b
    
    # p0 is the weight between neighboring pixels
    def p0(self, p0):
        self.p0 = p0

    def segmentImage(self, I):
        n = len(I)

        # get residuals matrix (starts off as capactities)
        # we only need last residual matrix, so no need for flow graph
        residuals = self.constructAdjacencyMatrix(I).copy()

        hasPath = True
        while hasPath:
            # source and sink
            s = n**2
            t = n**2+1

            # add the source node to stack and seen
            stack = [s]
            seen = [s]
            parent = np.full([n**2+2], -1)
    
            # get the bottleneck for the path
            bottleneck = 422
            while parent[t] == -1 and stack: 
                # pop last node
                v = stack.pop()
    
                # if edge value is not 0, node is adjacent
                # add adjacent node to path if its not in stack or path already
                for i in range(n**2+2): 
                    if i not in seen and residuals[v][i] > 0: 
                        stack.append(i) 
                        seen.append(i)
                        parent[i] = v
                
            # if successful path:
            if parent[t] != -1:
                # get bottleneck
                while t != s:
                    bottleneck = min(bottleneck, residuals[parent[t]][t])
                    t = parent[t]
                
                # update matrix
                t = n**2+1
                while t != s:
                    # subtract bottleneck along path
                    residuals[parent[t]][t] -= bottleneck
              
                    # add bottleneck against path
                    residuals[t][parent[t]] += bottleneck

                    t = parent[t]
                
                # iterate again
                hasPath = True

            # else return false and end FF in main function   
            else: 
                # path is set A (foreground) plus source
                A = set(seen) - set([n**2])
                hasPath = False

        # A is now set, use it to set foreground=1
        # default pixels to background=0
        output = np.zeros([n, n])
        # convert nodes back to coordinates
        for v in A:
            coord_v = np.array([v//n, v%n])
            output[coord_v[0]][coord_v[1]] = 1

        return output
            

    def constructAdjacencyMatrix(self, I):
        # source: n**2, sink: n**2+1
        n = len(I)
        edges = np.zeros([n**2+2, n**2+2])
        for x in range(n**2):
            # coordinate of x
            coord_x = np.array([x//n, x%n])

            # get a(x) and b(x)
            a = 442 - round(np.linalg.norm(I[coord_x[0], coord_x[1]] - I[self.x_a[0], self.x_a[1]]))
            b = 442 - round(np.linalg.norm(I[coord_x[0], coord_x[1]] - I[self.x_b[0], self.x_b[1]]))

            # add b(x) weight in (x,t)
            edges[x, n**2+1] = b
            
            # add a(x) weight in (s, x)
            edges[n**2, x] = a
            
            # add p(x) weight
            # get cord of x
            for j in range(n**2):
                coord_j = np.array([j//n, j%n])
                dist = np.linalg.norm(coord_x - coord_j)

                if dist < 2 and (coord_x != coord_j).any():
                    edges[x, j] = self.p0
                    edges[j, x] = self.p0
        
        return edges
    
  



        
        

   

