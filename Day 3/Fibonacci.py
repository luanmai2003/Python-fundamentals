def fib(n):
    a, b = 0, 1
    # a = 0; b = 1 \\ a = 1; b = 1 \\ a = 1; b = 2 \\ a = 2; b = 3 \\ a = 3; b = 5 ...
    while a < n:
        # 0 < 5000 \\ 1 < 5000 \\ 1 < 5000 \\ 2 < 5000 \\ 3 < 5000 ...
        print(a, end=' ')
        # print 0 \\ print 1 \\ print 1 \\ print 2 \\ print 3 ...
        a, b = b, a+b
        # a = 1; b = 1 \\ a = 1; b = 2 \\ a = 2; b = 3 \\ a = 3; b = 5 \\ a = 5; b = 8 ...
fib(100)

# #########################################################################

def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

print(fib2(100))     