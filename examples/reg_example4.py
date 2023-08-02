import re

text = 'abbaaabbbbaaaaa'

pat = 'ab'

for match in re.findall(pat, text):
    print 'Found "%s"' % match