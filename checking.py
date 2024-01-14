    def __iterateFF(self):
        # source and sink
        s = self.n**2
        t = self.n**2+1

        # add the source node to stack and seen
        stack = [s]
        seen = [s]
        parent = np.full([self.n**2+2], -1)
  
        # get the bottleneck for the path
        # max cut = min flow
        bottleneck = 422
        while parent[t] == 0 and stack: 
            # pop last node, add to path
            v = stack.pop()
  
            # if edge value is not 0, node is adjacent
            # add adjacent node to path if its not in stack or path already
            for i in range(self.n**2+2): 
                if i not in seen and self.residuals[v, i] > 0: 
                    stack.append(i) 
                    parent[i] = v
             
        # if successful path:
        if parent[t] != 0:
            # get bottleneck
            while t != s:
                bottleneck = min(bottleneck, self.residuals[parent[t]][t])
                t = parent[t]
                

            # update matrix
            while t != s:
                # subtract bottleneck along path
                self.residuals[parent[t], ]

                # add bottleneck against path

                t = parent[t]
            
            # iterate again
            return True

        # else return false and\\\\\\\\\\\
        #  end FF in main function   
        else: 
            # path is set A (foreground) plus source
            self.A = set(path) - set([self.n**2])
            return False
        

 def __iterateFF(self):
        # source and sink
        s = self.n**2
        t = self.n**2+1

        # add the source node to stack and seen
        stack = [s]
        seen = [s]
        path = []
  
        # get the bottleneck for the path
        # max cut = min flow
        bottleneck = 422
        while (t not in path) and stack:
            # pop last node, add to path
            v = stack.pop()
            # path.append(v)
            seen.append(v)
  
            # if edge value is not 0, node is adjacent
            # add adjacent node to path if its not in stack or path already
            for i in range(self.n**2+2): 
                if i not in seen and self.residuals[v][i] != 0: 
                    stack.append(i) 
                    # seen.append(i)
                    path.append(i)

        
        print(path)
        # if successful path:
        if t in path:
            # get bottleneck
            for index in range(0, len(path) - 1):
                if self.residuals[path[index]][path[index + 1]] < bottleneck:
                    # print(self.residuals[path[index]][path[index + 1]])
                    bottleneck = self.residuals[path[index]][path[index + 1]]
               

            # update matrix
            for index in range(0, len(path) - 1):
                # subtract bottleneck along path
                self.residuals[path[index]][path[index + 1]] -= bottleneck

                # add bottleneck against path
                self.residuals[path[index + 1]][path[index]] += bottleneck
            
            # iterate again
            return True

        # else return false and end FF in main function   
        else: 
            # path is set A (foreground) plus source
            self.A = set(path) - set([self.n**2])
            return False
