import numpy as np 
# create edges matrix
# source: n**2, sink: n**+1
n = 3
edges = np.zeros([n**2+2, n**2+2])
I = np.zeros([3,3,3])
I[2,2,0]=128
I[1,2,0]=128
x_a = np.array([2,2])
x_b = np.array([0,0])
p0 = 1

for x in range(n**2):
    # coordinate of x
    coord_x = np.array([x//n, x%n])

    # get a(x) and b(x)
    a = 442 - round(np.linalg.norm(I[coord_x[0], coord_x[1]] - I[x_a[0], x_a[1]]))
    b = 442 - round(np.linalg.norm(I[coord_x[0], coord_x[1]] - I[x_b[0], x_b[1]]))

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
            edges[x, j] = p0
            edges[j, x] = p0

print(edges)
