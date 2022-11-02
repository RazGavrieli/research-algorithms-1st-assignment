
import functools
import collections



def print_sorted(x):
    """
    prints sorted dictionaries, tuples, sets and lists (that are combined)
    """
    print_sorted_inner_recursion_function(x)

def print_sorted_inner_recursion_function(x, Key=None):
    if Key!= None:
        print(Key, end=": ")
    
    if type(x) == tuple:
        x.sort(key=functools.cmp_to_key(compare))
        for i in x:
            print_sorted_inner_recursion_function(i)
    elif type(x) == list:
        x.sort(key=functools.cmp_to_key(compare))
        for i in x:
            print_sorted_inner_recursion_function(i)
    elif type(x) == set:
        xAsList = list(x)
        print_sorted_inner_recursion_function(xAsList)
    elif type(x) == dict:
        xAsOrderedDict = collections.OrderedDict(sorted(x.items()))
        for i in xAsOrderedDict:
            print_sorted_inner_recursion_function(xAsOrderedDict.get(i), i)
    else:
        print(x, end=" ")

def compare(item1, item2):
    # if item 1 and item 2 are comparable
    try: 
        if item1 < item2:
            return -1
        elif item1 > item2:
            return 1
        else:
            return 0
    # if the two items are not comparable, return that they are equal
    except: 
        return 0

if __name__ == "__main__":
    x = {'a':5, 'c':{4, 3, 6}, 'b': [[3,2], [12, 32, 1,3], [5]]}
    print_sorted(x)
    print()
    x = [1, -2, {'c':[3, 2, 1], 'a': {2: 'world', 1:'hello'}, 'g':4}, [4, 3, 5]]
    print_sorted(x)
    print()


