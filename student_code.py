import math
from heapdict import heapdict


def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def manhattan_distance(x1, y1, x2, y2):
    
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    
    D = 1
    
    return D * (dx + dy)


def heuristic(position_1, position_2):
    '''
    In this heuristic, I tried the following both approaches:
    1. Manhattan distance 
       It is usually used for finding the minimum cost D for moving from one space to an adjacent space
    2. Euclidean distance
       The straight line distance between two nodes
    
    Both worked pretty well. Since the heuristic I am using here is to calculate the distance between adjacent nodes,
    Manhattan distance is more efficient in this case. 
    Ref: http://theory.stanford.edu/~amitp/GameProgramming/Heuristics.html#S7
    
    I found another heuristics I could try -> diagonal distance, e.g.
    
    def diagonal_distance(x1, y1, x2, y2) =
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        
        return D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
        
    with variants:
    D=1 D2=1        ->  Chebyshev distance
    D=1 D2=sqrt(2)  ->  octile distance
    
    Summary of three heuristics
    * Manhattan Distance: D * (dx + dy)
      -> When We are allowed to move only in four directions only (right, left, top, bottom)
    * Diagonal Distance:  D * (dx + dy) + (D2 - 2 * D) * min(dx, dy)
      -> We are allowed to move in eight directions only (similar to a move of a King in Chess)
    * Euclidean Distance: sqrt((x1 - x2)**2 + (y1 - y2)**2)
      -> We are allowed to move in any directions
      
    where: dx = abs(x1 - x2) and dy = abs(y1 - y2)
    
    Ref: https://www.geeksforgeeks.org/a-search-algorithm/
    '''
        
    x1 = position_1[0]
    y1 = position_1[1]
    
    x2 = position_2[0]
    y2 = position_2[1]
    
    # return euclidean_distance(x1, y1, x2, y2)
    return manhattan_distance(x1, y1, x2, y2)


def backtrace(goal, lookup_preceed_node):
    path = list()
    
    node = goal
    while True:
        path.insert(0, node)
        preceed_node = lookup_preceed_node[node]
        if preceed_node != node:
            node = preceed_node
        else:
            break
        
    return path


def shortest_path(M,start,goal):
    
    frontier = heapdict()
    frontier[start] = 0.
    
    explored = set()
    
    lookup_preceed_node = {start: start}
    
    while frontier:
        
        current_node, current_node_cost = frontier.popitem()
        
        for next_node in M.roads[current_node]:
            
            if next_node in explored:
                continue
                
            next_node_cost = current_node_cost + heuristic(M.intersections[current_node], M.intersections[next_node]) 

            if next_node_cost < frontier.get(next_node, math.inf):
                frontier[next_node] = next_node_cost
                lookup_preceed_node[next_node] = current_node
        
        explored.add(current_node)
    
    return backtrace(goal, lookup_preceed_node) if goal in lookup_preceed_node else None