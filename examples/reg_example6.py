
import re

text = 'abbaaabbbbaaaaa'

pattern = 'ab'
print ">>",re.finditer(pattern, text)
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print 'Found "%s"=="%s" at %d:%d' % (match.re.pattern,text[s:e], s, e)