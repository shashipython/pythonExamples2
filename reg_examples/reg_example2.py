import re

pattern = 'this'
text = 'Does this text this match the this pattern?'
print "RE path:",type(re)

ma = re.search(pattern, text)
print "====>\n",ma
print "Objs:",ma,"List of all attribute and method:",dir(ma)
print "\nPath:",type(ma)
s = ma.start()
e = ma.end()

print "Found %s in %s from %d to %d (%s)" % \
    (ma.re.pattern, ma.string, s, e, text[s:e])
