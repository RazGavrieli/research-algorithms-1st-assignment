"""
>>> breadth_first_search(start=(0,0), end=(2,2), neighbor_function=lattice_graph)
[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]

>>> breadth_first_search(start=(0,0), end=(2,-2), neighbor_function=lattice_graph)
[(0, 0), (1, 0), (2, 0), (2, -1), (2, -2)]


>>> breadth_first_search(start=(0,0), end=(0,-2), neighbor_function=lattice_graph)
[(0, 0), (0, -1), (0, -2)]

>>> breadth_first_search(start=(0,0), end=(6,-2), neighbor_function=lattice_graph)
[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (6, -1), (6, -2)]

>>> len(breadth_first_search(start=(0,0), end=(2, 2), neighbor_function=lattice_graph))
5

>>> breadth_first_search(start='A', end='F', neighbor_function=dict_graph_neighbor_function)
['A', 'C', 'F']

>>> breadth_first_search(start='A', end='E', neighbor_function=dict_graph_neighbor_function)
['A', 'B', 'E']

    End node is not reachable from Start node
    >>> breadth_first_search(start='A', end='G', neighbor_function=dict_graph_neighbor_function)
    Traceback (most recent call last):
    ...
    Exception: could not find destination node
"""

def breadth_first_search(start, end, neighbor_function):
    """
    Generic function that can perform a BFS on a generic type of a graph. 
    Usage examples:
    BFS on a grid graph    
    >>> breadth_first_search(start=(0,0), end=(6,-2), neighbor_function=lattice_graph)
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (6, -1), (6, -2)]

    Graph that is represented by a dictionary
    >>> breadth_first_search(start='A', end='F', neighbor_function=dict_graph_neighbor_function)
    ['A', 'C', 'F']

    End node is not reachable from Start node
    >>> breadth_first_search(start='A', end='G', neighbor_function=dict_graph_neighbor_function)
    Traceback (most recent call last):
    ...
    Exception: could not find destination node
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

    raise Exception("could not find destination node")


def lattice_graph_w(node):
    """
    returns the neighbors of a node in grid graph w
    """
    (x, y) = node
    return [(x+1, y), (x-1, y), (x, y+1), (x,y-1), (x+1, y+1), (x+1, y-1), (x-1, y+1), (x-1, y-1)]

def lattice_graph(node):
    """
    returns the neighbors of a node in grid graph
    """
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
    import doctest
    doctest.testmod(verbose=True)