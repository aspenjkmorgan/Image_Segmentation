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
        self.n = len(I)

        # get residuals matrix (starts off as capactities)
        self.residuals = self.constructAdjacencyMatrix(I)

        hasPath = True
        while hasPath:
            # if there is a path, run dfs and update matrix
            hasPath = self.__iterateFF()

        # A is now set, use it to set foreground=1
        # default pixels to background=0
        output = np.zeros([self.n, self.n])
        # convert nodes back to coordinates
        for v in self.A:
            coord_v = np.array([v//self.n, v%self.n])
            output[coord_v[0], coord_v[1]] = 1

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
    
    def __iterateFF(self):
        # source and sink
        s = self.n**2
        t = self.n**2+1

        # create a stack and a path array
        stack = [] 
        path = []
  
        # add the source node to stack
        stack.append(s) 
  
        # get the bottleneck for the path
        bottleneck = 422
        while t not in path and stack: 
            # pop last node, add to path
            v = stack.pop()
            path.append(v) 
  
            # if edge value is not 0, node is adjacent
            # add adjacent node to path if its not in stack or path already
            for i in range(self.n**2+2): 
                if i not in stack and i not in path and self.residuals[v, i] != 0: 
                    stack.append(i)  
                    if self.residuals[v, i] < bottleneck:
                        bottleneck = self.residuals[v, i]
            print(stack)
                        
        # if successful path, update matrix
        if t in path:
            for index in range(1, len(path)):
                # subtract bottleneck along path
                self.residuals[path[index - 1], path[index]] -= bottleneck

                # add bottleneck against path
                self.residuals[path[index], path[index - 1]] += bottleneck
            
            # iterate again
            return True

        # else return false and end FF in main function   
        else: 
            # path is set A (foreground) plus source
            self.A = set(path) - set([self.n**2])
            return False



        
        

   

