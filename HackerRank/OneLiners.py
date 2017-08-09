def upto():
    print(*range(1, int(input())+1), sep='')


def triples():
    x, y, z, n = (int(input("Give me an int: ")) for _ in range(4))
    print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1) for c in range(0, z+1) if a + b + c == n])


def second_max():
    nums = map(int, input().split())
    print(sorted(list(set(nums)))[-2])


def swapcase(s):
    return s.swapcase()


def swapcase2():
    return ''.join([i.lower() if i.isupper() else i.upper() for i in input()])


def split_and_join(s):
    return "-".join(s.split(" "))


def welcome():
    firstname, lastname = input("What is your full name?  ").split()
    print("Hello {0} {1}! This line is done with new formatting!".format(firstname, lastname))
    print("But did you know, %s, that depricated formatting still works!" % firstname)


def count_substring(string, substring):
    # len(string) - len(substring) + 1 == count for the sliding window
    # string[i:i + len(substring)] == slice of the string that is currently compared to the substring
    return sum([1 for i in range(len(string) - len(substring) + 1) if string[i:i + len(substring)] == substring])


def string_checker(string):
    for test in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print("For {0} test and {1} string:".format(test, string), any(eval("char." + test + "()") for char in string))

