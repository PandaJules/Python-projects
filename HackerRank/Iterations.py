from itertools import product
from itertools import permutations
from itertools import combinations
from functools import reduce


def cross_product(list1, list2):
    ab = list(product(list1, list2))
    print(*ab, sep=' ')


def perm(iterable, length):
    # the order matters
    print(*[''.join(str(i)) for i in permutations(iterable, length)], sep='\n')


def comb(iterable, length):
    # order does not matter - fewer items than permutations
    print(*[''.join(i) for i in combinations(iterable, length)], sep='\n')


# Other function to use: combinations_with_replacement

def frequencies():
    # output (frequency, symbol) for consecutive repeated symbols
    from itertools import groupby
    print(*[(len(list(c)), int(k)) for k, c in groupby(input())])


def n_fibonacci_to_m(n, m):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 2] + fib[i - 1])
    cube = lambda x: pow(x, m)
    print("List of", n, "fibonacci numbers to the power", m, "is\n", list(map(cube, fib)))


def list_sum(lst):
    print("Sum of the list", lst, "is\n", reduce(lambda x, y: x + y, lst))


def list_product(lst):
    print("Product of the list", lst, "is\n", reduce(lambda x, y: x * y, lst))
