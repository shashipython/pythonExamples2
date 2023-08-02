import re


def std_count(fname,k):
    c=0
    fd=open(fname,'r')
    reg=re.compile('shiva')
    total=0
    for line in fd.readlines():
        r1=reg.findall(line) #['shiva','shiva']
        if r1:
            p=r1.__len__()
            total=total+p
            print "Line:",c,"Count:",p
        #if k in line:
        #    print "Line:",c,"Count:",line.count(k)
        c=c+1
    print "Total count",total

std_count('std_report_2.txt','shiva')