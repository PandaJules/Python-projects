import re

# \s matches any whitespace character \r\n\t\f
# \d matched any digit 0-9
# \w will match any word character: alphanumeric characters and underscores
# [^] matches whatever is NOT inside of brackets
# X{n} matches X n times
# * is 0 or more, + is 1 or more
# \b assert position at a word boundary
regex_pattern1 = r'\.{2,5}$'    # from 2 to 5 dots inclusively
regex_pattern2 = r'\d{3,}$'		# 3 or more digits
regex_pattern3 = r'^(Mr|Mrs|Ms|Dr|Er)\.[A-Za-z]+$'  # () for group capturing and | for OR

ipv4 = r'^((1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.){3}(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$'
ipv6 = r'^([0-9a-f]+:){7}[0-9a-f]+$'

def findall():
    test_string1 = input()
    regex_pattern = r'the'
    match = re.findall(regex_pattern, test_string1)
    print("Number of matches:   ", len(match))


def match():
    # re.match() is anchored at the beginning of the string
    regex_pattern = r'..\...'
    test_string = input("Something to match "+regex_pattern+" : ")
    match = re.match(regex_pattern, test_string)
    print("Number of matches:   ", len(match))


def search():
    # re.search() scans through the whole string
    regex_pattern = r'\d\d\D\d\d$'
    test_string = input("Something to match "+regex_pattern+" : ")
    match = re.search(regex_pattern, test_string).group()
    print("Number of matches:   ", len(match))

    regex_pattern = r'\S\S\S\s\S\S\S$'
    test_string = input("Something to match "+regex_pattern+" : ")
    match = re.search(regex_pattern, test_string).group()
    print("Number of matches:   ", len(match))


def is_valid_regex(regex):
    try:
        re.compile(regex)
        print(regex, "is a valid regex")
    except re.error:
        print(regex, "is not a valid regex")
