import sys

"""
Convert AM/PM format to 24hr format
"""


def timeConversion(t):
    if t[8] == "P" and t[:2] != "12":
            t = str(int(t[:2])+12) + t[2:]
    if t[8] == "A" and t[:2] == "12":
            t = "00" + t[2:]
    return t[:-2]


s = input().strip()
result = timeConversion(s)
print(result)
