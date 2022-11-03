from bfs import *

if __name__ == "__main__":
    print(breadth_first_search(start=(0,0), end=(2,2), neighbor_function=lattice_graph))
    # This example uses the 'visited' queue to break the loop and return None
    #print(breadth_first_search(start='A', end='G', neighbor_function=dict_graph_neighbor_function))
    print(breadth_first_search(start='A', end='F', neighbor_function=dict_graph_neighbor_function))
    
    #    --> A -> B ---> D
    #    |   |    |     
    #    |   V    V
    #    |   C    E
    #    |   \    /
    #    |    V  V
    #    -----  F