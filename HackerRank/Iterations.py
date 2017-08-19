from itertools import product
from itertools import permutations
from itertools import combinations


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