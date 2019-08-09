import re

s = 'a b c'

groups = re.findall('(.)\s', s)

print(groups)