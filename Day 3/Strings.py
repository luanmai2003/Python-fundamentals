def my_function():
    """
    Name: Luan
    age: 21
    """
    pass
print(my_function.__doc__)

# #########################################################################

def f(ham: str, eggs: str = 'eggss') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)

f('spam')
# Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
# Arguments: spam eggs