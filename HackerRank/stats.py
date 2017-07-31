import numpy as np
from scipy import stats

numbers = list(map(int, input("Give me an array: ").split()))
print("Mean of this list of numbers is", np.mean(numbers))
print("Median of this list of numbers is", np.median(numbers))
print("Mode of this list of numbers is", int(stats.mode(numbers)[0]))

nums = [int(x) for x in input("Give me another array: ").split()]
weights = [int(x) for x in input("What are the weights: ").split()]
print(round(sum([i[0]*i[1] for i in zip(nums, weights)])/sum(weights), 1))
