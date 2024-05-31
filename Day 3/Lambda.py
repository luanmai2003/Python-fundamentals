add = lambda a, b: a + b
result = add(3, 5)
print(result)


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(0))
# 42
print(f(1))
# 43
print(f(4))
# 46


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)
# Kết quả: [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]