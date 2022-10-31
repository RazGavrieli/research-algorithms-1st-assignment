# sources
# https://www.geeksforgeeks.org/function-annotations-python/
# https://docs.python.org/3/library/inspect.html
# import inspect
# I have decided to NOT import inspect to save resources
def f(x: int , y: float, z):
    return x+y+z

def safe_call(f, *args, **kwargs):
    """
    ensures correctness of a given list of arguments. 
    Raises exceptions if there are unmatching types or missing arguments
    """
    allVarnamesList = list(f.__code__.co_varnames) # Convert a tuple of f's arguments to a list (mmutable)
    annotationsDict = f.__annotations__ # Get a dictionary of all f's annotated arguments 
    # for each argument given to safe_call
    for key, value in kwargs.items():
        # if key is not an argument of f 
        if key not in allVarnamesList: 
            raise Exception("unexpected arguments given to safe_call")
        # Remove the key from the variables names list
        allVarnamesList.remove(key)
        # if the type of the given variable does not match the type annotated in f
        if type(value) != annotationsDict.get(key) and key in annotationsDict.keys():
            raise Exception("unmatching types")
    
    # For each value given without an argument's name, assign an empty argument to it
    for arg in args:
        if len(allVarnamesList) != 0:
            for index, varName in enumerate(allVarnamesList):
                if annotationsDict.get(varName) == type(arg):
                    kwargs[varName] = arg
                    allVarnamesList.pop(index)
        else: # If we were given an positional value but we don't have an empty argument for it
            raise Exception("too many arguments given")
            
    # Define the number of default arguments in f
    numOfDefaults = 0 if f.__defaults__ == None else len(f.__defaults__)
    # If allVarnamesList is not empty, then there are arguments of f that wasn't assigned a value
    if len(allVarnamesList) - numOfDefaults > 0:
        raise Exception("missing arguments")

    return f(**kwargs)
 
if __name__ == "__main__":
    print(safe_call(f, 3.4, 4, z=3))
