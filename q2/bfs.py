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
        if node == end:
            return path
        for neighbour in neighbor_function(node):
            if neighbour not in visited:
                visited.append(neighbour)
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)


def func(node):
    (x, y) = node
    return [(x+1, y), (x-1, y), (x, y+1), (x,y-1)]\
        
if __name__ == "__main__":
    print(breadth_first_search(start=(0,0), end=(2,2), neighbor_function=func))