import pytest
from bfs import *

def four_neighbor_function(node)->list:
    (x, y) = node
    return [(x+1, y), (x-1, y), (x, y+1), (x,y-1)]

def dict_graph_neighbor_function(node):
    graph = {
    'A' : ['B','C'],            #        A -> B ---> D
    'B' : ['D', 'E'],           #        |    |     
    'C' : ['F'],                #        V    V
    'D' : [],                   #        C    E
    'E' : ['F'],                #        \    /
    'F' : []                    #         V  V
    }                           #           F
    return graph.get(node)

def test_1():
    expectedResult = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
    assert breadth_first_search(start=(0,0), end=(2,2), neighbor_function=four_neighbor_function) == expectedResult

def test_2():
    expectedResult = [(0, 0), (1, 0), (2, 0), (2, -1), (2, -2)]
    assert breadth_first_search(start=(0,0), end=(2,-2), neighbor_function=four_neighbor_function) == expectedResult

def test_3():
    expectedResult = [(0, 0), (0, -1), (0, -2)]
    assert breadth_first_search(start=(0,0), end=(0,-2), neighbor_function=four_neighbor_function) == expectedResult

def test_4():
    expectedResult = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (6, -1), (6, -2)]
    assert breadth_first_search(start=(0,0), end=(6,-2), neighbor_function=four_neighbor_function) == expectedResult

def test_5():
    expectedResult = 5
    assert len(breadth_first_search(start=(0,0), end=(2, 2), neighbor_function=four_neighbor_function)) == expectedResult

def test_polymorphic_1():
    expectedResult = ['A', 'C' ,'F']
    assert breadth_first_search(start='A', end='F', neighbor_function=dict_graph_neighbor_function) == expectedResult

def test_polymorphic_2():
    expectedResult = ['A', 'B' ,'E']
    assert breadth_first_search(start='A', end='E', neighbor_function=dict_graph_neighbor_function) == expectedResult