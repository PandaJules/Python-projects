import numpy as np
from scipy import stats
import math

numbers = list(map(int, input("Give me an array: ").split()))
print("Mean of this list of numbers is", np.mean(numbers))
print("Median of this list of numbers is", np.median(numbers))
print("Mode of this list of numbers is", int(stats.mode(numbers)[0]))

nums = [int(x) for x in input("Give me another array: ").split()]
weights = [int(x) for x in input("What are the weights: ").split()]
print("Weighted mean is:", round(sum([i[0] * i[1] for i in zip(nums, weights)]) / sum(weights), 1))


def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return int((arr[n // 2 - 1] + arr[n // 2]) / 2)


def interquartilerange(arr, frequencies):
    full = []
    for a, f in zip(arr, frequencies):
        full += [a] * f
    full.sort()
    N = len(full)
    if N % 2 == 0:
        q3 = median(full[N // 2:])
    else:
        q3 = median(full[N // 2 + 1:])
    q1 = median(full[:N // 2])
    print(round(float(q3 - q1), 1))


def stddev(arr):
    mean = sum(arr) / len(arr)
    var = 0
    for a in arr:
        var += (a - mean) ** 2
    return round(math.sqrt(var / len(arr)), 1)


# Binomial
def comb(n, x):
    return math.factorial(n) / (math.factorial(x) * math.factorial(n - x))


def binom(x, n, p):
    return comb(n, x) * p ** x * (1 - p) ** (n - x)


def cum(n, p, low, high):
    return sum([binom(i, n, p) for i in range(low, high)])


sb = np.random.binomial(100, 0.2)
sg = np.random.geometric(p=0.35)


# Geometric
def geom(success, first_success_attempt):
    assert 0 <= success <= 1
    assert first_success_attempt >= 1
    return ((1 - success) ** (first_success_attempt - 1)) * success


# Poisson
def pois(mean, value):
    return math.exp(-mean) * mean ** value / math.factorial(value)


# Normal
def cdf(x, mean, std):
    # cumulative distribution function
    return 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


def pearson_correlation_coefficient():
    from statistics import mean, pstdev

    n = int(input())
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    top = sum([a * b for a, b in zip([i - mean(x) for i in x], [i - mean(y) for i in y])])
    bottom = n * pstdev(x) * pstdev(y)
    rho = top / bottom

    print(round(rho, 3))
