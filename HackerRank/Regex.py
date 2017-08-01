import re

# \s matches any whitespace character \r\n\t\f
# \d matched any digit 0-9
# \w will match any word character: alphanumeric characters and underscores
# [^] matches whatever is NOT inside of brackets
# X{n} matches X n times
# * is 0 or more, + is 1 or more
# \b assert position at a word boundary

test_string1 = input()
regex_pattern = r'the'
match = re.findall(regex_pattern, test_string1)
print("Number of matches:   ", len(match))


# re.match() is anchored at the beginning of the string
test_string2 = input()
regex_pattern = r'..\...'
match = re.match(regex_pattern, test_string2)
print("Number of matches:   ", len(match))

# re.search() scans through the whole string
test_string3 = input()
regex_pattern = r'\d\d\D\d\d$'
match = re.search(regex_pattern, test_string3).group()
print("Number of matches:   ", len(match))

test_string4 = input()
regex_pattern = r'\S\S\S\s\S\S\S$'
match = re.search(regex_pattern, test_string4).group()
print("Number of matches:   ", len(match))

regex_pattern1 = r'\.{2,5}$'    # from 2 to 5 dots inclusively
regex_pattern2 = r'\d{3,}$'		# 3 or more digits
regex_pattern3 = r'^(Mr|Mrs|Ms|Dr|Er)\.[A-Za-z]+$'  # () for group capturing and | for OR

ipv4 = r'^((1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])\.){3}(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$'
ipv6 = r'^([0-9a-f]+:){7}[0-9a-f]+$'



