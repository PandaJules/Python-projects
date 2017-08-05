def hor_or_ver():
    """Input:
    n - number of points in 2D
    <x> <y> - coordinates
    Output:
    YES/NO - whether the points all lie on a horizontal or vertical line"""
    n = int(input())
    xs = set()
    ys = set()
    for _ in range(n):
        x, y = map(int, input().split())
        xs.add(x)
        ys.add(y)
    if len(xs) == 1 or len(ys) == 1:
        print("YES")
    else:
        print("NO")
