# File: re-example-4.py

import re

text = "you're no fun anymore...1234"

# literal replace (string.replace is faster)
print re.sub("fun", "entertaining", text)

# collapse all non-letter sequences to a single dash
print re.sub("[^\w]+", "-", text)

# convert all words to beeps
print re.sub("\S+", "-BEEP-", text)


# convert all digit to *****
print re.sub("\d+", "*", text)
