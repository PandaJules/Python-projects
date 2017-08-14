def swapcase(s):
    print("This is swapped with a built-in function: ", s.swapcase())
    print("This is swapped with lower(), upper(): ",''.join([i.lower() if i.isupper() else i.upper() for i in input()]))


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


def number_systems(number):
    width = len(bin(number))-2
    for i in range(1, number+1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width))


def wrap(string, max_width):
    import textwrap
    return textwrap.fill(string, max_width)


def wrap_split(string, max_width):
    import textwrap
    return textwrap.wrap(string, max_width)


def capitalize_all(string):
    return " ".join([word.capitalize() for word in string.split(" ")])


def alpha_pattern():
    import string
    alphabet = string.ascii_lowercase
    n = len(alphabet)
    line = []
    for i in range(n):
        s = "-".join(alphabet[i:n])
        line.append((s[::-1] + s[1:]).center(4 * n - 3, "-"))
    print('\n'.join(line[:0:-1] + line))
