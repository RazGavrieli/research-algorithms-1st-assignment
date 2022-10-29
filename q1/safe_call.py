# source
# https://www.geeksforgeeks.org/function-annotations-python/

def f(x: int , y: float, z):
    return x+y+z

def ssafe_call(f, *args, **kwargs):
    """
    Compares the given list of arguments with the arguments of a given function
    """
    print()
    # Compare types of each annotated arguments
    annotationsDict = f.__annotations__
    for i in annotationsDict.keys():
        if annotationsDict.get(i) != type(kwargs.get(i)):
            print(i)
            if i not in kwargs.keys():
                raise Exception("missing arguments")
            else:
                raise Exception("unmatching types")
            

    # Check for unexpected argument
    for i in kwargs.keys():
        print(i, annotationsDict, f.__defaults__)
        if f.__defaults__ != None:
            if i not in annotationsDict or i not in f.__defaults__:
                raise Exception("unexpected arguments given to safe_call")
        else:
            if i not in annotationsDict:
                raise Exception("unexpected arguments given to safe_call")


    # Define the number of default arguments in f
    numOfDefaults = 0 if f.__defaults__ == None else len(f.__defaults__)
    if len(kwargs) < f.__code__.co_argcount - numOfDefaults:
        raise Exception("missing arguments")
    
    return f(**kwargs)

def safe_call(f, **kwargs):
    """
    ensures correctness of a given list of arguments. 
    Raises exceptions if there are unmatching types or missing arguments
    """
    annotationsDict = f.__annotations__
    # for each argument given to safe_call
    for key, value in kwargs.items():
        # if key is not an argument of f 
        if key not in f.__code__.co_varnames: 
            raise Exception("unexpected arguments given to safe_call")
        # if the type of the given variable does not match the type annotated in f
        if type(value) != annotationsDict.get(key) and key in annotationsDict.keys():
            raise Exception("unmatching types")
    
    # Define the number of default arguments in f
    numOfDefaults = 0 if f.__defaults__ == None else len(f.__defaults__)
    if len(kwargs) < f.__code__.co_argcount - numOfDefaults:
        raise Exception("missing arguments")

    return f(**kwargs)

if __name__ == "__main__":
    print(simple_safe_call(f, x=1, y=5.0, z=3))
