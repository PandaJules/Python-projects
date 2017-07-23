import sys

"""
Input in the form:
n - length of the string
s - string to convert with the Caesar cipher
k - Caesar shift
"""

n = int(input().strip())
s = input().strip()
k = int(input().strip())

for i in range(n):
    letter = s[i]
    if 65 <= ord(letter) <= 90:
        h = (ord(letter)-65+k) % 26 + 65
        s = s[:i]+chr(h)+s[i+1:]
    elif 97 <= ord(letter) <= 122:
        h = (ord(letter)-97+k) % 26 + 97
        s = s[:i]+chr(h)+s[i+1:]
print(s)