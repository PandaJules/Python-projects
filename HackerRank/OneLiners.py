def upto():
    print(*range(1, int(input())+1), sep='')


def triples():
    x, y, z, n = (int(input("Give me an int: ")) for _ in range(4))
    print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a + b + c == n])


def second_max():
    nums = map(int, input().split())
    print(sorted(list(set(nums)))[-2])




