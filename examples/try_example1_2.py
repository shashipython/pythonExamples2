import string, sys

try:
    f = open('test1.txt','r')
    s = f.readline()
    i = int(string.strip(s))
except (IOError,ValueError):
    print "Opps Got Exception"
except:
    print "Unexpected error:", sys.exc_info()
finally:
    f.close()
    print "I am closing file"