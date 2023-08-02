import re


def word_count(fname):
    c=0
    fd=open(fname,'r')
    reg=re.compile('\w+')
    total=0
    wc=0
    dc=0
    fd1=open('test_std.txt','w')
    for line in fd.readlines():
        l1=line.upper()
        fd1.write(l1)
        r1=reg.findall(line)
        for i in r1:
            if i.isalpha() or not i.isdigit():
                wc=wc+1
            if i.isdigit():
                dc=dc+1
        c=c+1
    fd.close()
    fd1.close()
    print "Total lines:",c
    print "Total words:",wc
    print "Total digit",dc

word_count('std_row.txt')