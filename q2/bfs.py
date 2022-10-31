def breadth_first_search(start, end, neighbor_function):
    """
    Generic function that can perform a BFS on a generic type of a graph. 
    start node
    end node
    neighbor_function gets a node and returns its neighbors
    """
    visited = []    # List for visited nodes.
    queue = []      # Initialize a queue
    visited.append(start)
    queue.append([start])

    while queue:          # Creating loop to visit each node
        path = queue.pop(0) 
        node = path[-1]
        if node == end: # This causes the search to stop whenever we find the destination
            return path
        for neighbour in neighbor_function(node):
            if neighbour not in visited: # This causes the search to stop if we can't find the end
                visited.append(neighbour)
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)


def func(node):
    (x, y) = node
    return [(x+1, y), (x-1, y), (x, y+1), (x,y-1)]

def dict_graph_neighbor_function(node):
    graph = {
    'A' : ['B','C'],            #    --> A -> B ---> D
    'B' : ['D', 'E'],           #    |   |    |     
    'C' : ['F'],                #    |   V    V
    'D' : [],                   #    |   C    E
    'E' : ['F'],                #    |   \    /
    'F' : ['A']   # cycle       #    |    V  V
    }                           #    -----  F
    return graph.get(node)
        
if __name__ == "__main__":
    print(breadth_first_search(start=(0,0), end=(2,2), neighbor_function=func))
    # This example uses the 'visited' queue
    print(breadth_first_search(start='A', end='G', neighbor_function=dict_graph_neighbor_function))