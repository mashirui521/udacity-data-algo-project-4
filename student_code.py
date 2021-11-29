import math
from heapdict import heapdict

def euclidean_distance(position_1, position_2):
    x1 = position_1[0]
    y1 = position_1[1]
    
    x2 = position_2[0]
    y2 = position_2[1]
    
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def shortest_path(M,start,goal):
    
    # frontier = {start: 0}
    frontier = heapdict()
    frontier[start] = 0
    
    explored = set()
    
    lookup_preceed_node = {start: start}
    
    # A* search
    while frontier:
        
        current_node, current_node_cost = frontier.popitem()
        
        for next_node in M.roads[current_node]:
            
            if next_node not in explored:
                
                next_node_cost = current_node_cost + euclidean_distance(M.intersections[current_node], M.intersections[next_node]) + euclidean_distance(M.intersections[next_node], M.intersections[goal])
                
                if next_node_cost < frontier.get(next_node, math.inf):
                    frontier[next_node] = next_node_cost
                    lookup_preceed_node[next_node] = current_node
        
        explored.add(current_node)
    
    # path not found
    if goal not in lookup_preceed_node:
        return None
    
    # backtrace
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