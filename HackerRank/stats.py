import numpy as np
from scipy import stats
import math


numbers = list(map(int, input("Give me an array: ").split()))
print("Mean of this list of numbers is", np.mean(numbers))
print("Median of this list of numbers is", np.median(numbers))
print("Mode of this list of numbers is", int(stats.mode(numbers)[0]))

nums = [int(x) for x in input("Give me another array: ").split()]
weights = [int(x) for x in input("What are the weights: ").split()]
print(round(sum([i[0]*i[1] for i in zip(nums, weights)])/sum(weights), 1))


def median(arr):
    n = len(arr)
    if n%2==1:
        return arr[n//2]
    else:
        return int((arr[n//2-1]+arr[n//2])/2)

def interquartilerange(arr, frequencies):
	full = []
	for a, f in zip(arr, frequencies):
	    full += [a]*f
	full.sort()
	N = len(full)
	if (N % 2 == 0):
	    q3 = median(full[N//2:])
	else:
	    q3 = median(full[N//2+1:])
	q1 = median(full[:N//2])
	print (round(float(q3-q1), 1))

def stddev(arr):
	mean = sum(arr)/len(arr)
	var = 0
	for a in arr:
	    var += (a-mean)**2
	return(round(math.sqrt(var/n),1))