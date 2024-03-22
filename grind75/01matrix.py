from typing import Type, List, Tuple
import queue



"""
We have a MxN binary matrix. For each cell we want to return the nearest distance to a 0
The distance between two adjacent cells is 1

Approach:
- For each cell, do a BFS to find the nearest 1; then return that as an int
O(|V|+|E|)
- Assign that to the return matrix; return that matrix after iterating over
all the cells
"""

input1 = [[0,0,0],[0,1,0],[0,0,0]]
expected1 =  [[0,0,0],[0,1,0],[0,0,0]]

input2 = [[0,0,0],[0,1,0],[1,1,1]]
expected2 = [[0,0,0],[0,1,0],[1,2,1]]

type Matrix = List[List[int]]

directions = [(0,1),(0,-1),(1,0),(-1,0)]

def is_valid_direction(dx,dy,n):
    return dx >= 0 and dx < n and dy >= 0 and dy < n

def get_distance_to_zero(origin : Tuple[int,int], m : Matrix) -> int:
    queue = [origin]
    visited = []
    n = len(m)

    dist = 0
    while queue:
        x,y = queue.pop()
        print(f"Current node {x,y}")
        visited.append((x,y))

        # If the current node is zero, return the distance
        if m[x][y] == 0:
            return dist

        # If not, iterate over neighbors
        for dirx,diry in directions:
            dx, dy = x+dirx, y+diry
            if (dx,dy) not in visited and is_valid_direction(dx,dy,n):

                # If the neighbor is zero, return it
                if m[dx][dy] == 0:
                    print("Found zero, returning")
                    dist += 1
                    return dist
                print(f"Appending direction {dx,dy}")
                queue.append((dx,dy))
        dist += 1

    return dist

def get_distances(m):
    n = len(m)
    resp = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(n):
        for j in range(n):
            dist = get_distance_to_zero((i,j),m)
            print(i,j)
            resp[i][j] = dist
    return resp

print(get_distance_to_zero((2,1), input2))
print(get_distances(input1))
