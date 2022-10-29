
from typing import Dict, Set, Tuple

import collections

def print_sorted(x, key=None):
    if key!= None:
        print(key, end=": ")

    if type(x) == tuple:
        x.sort()
        for i in x:
            print_sorted(i)
    elif type(x) == list:
        x.sort()
        for i in x:
            print_sorted(i)
    elif type(x) == set:
        x.sort()
        for i in x:
            print_sorted(i)
    elif type(x) == dict:
        od = collections.OrderedDict(sorted(x.items()))
        for i in od:
            print_sorted(od.get(i), i)
    else:
            print(x, end=" ")


if __name__ == "__main__":
    x = {'a':5, 'c':{4, 3, 6}, 'b': [[3,2], [12, 32, 1,3], [5]]}
    print_sorted(x)
    print()
    x = [1, 2, 3]
    print_sorted(x)
    print()
