import re

#reg=re.compile(r'([\w\.\-\:\/]+)\s*(up|down)\s*(up|down).*')
reg=re.compile(r'([\w\-\/\:\.]+)\s*(up|down)\s*(up|down)\s*(\w+)\s*([\d\.]+).*')
def reg_match_int(fileName):
    out_dict={}
    fd=open(fileName,'r')
    for line in fd.readlines():
        regMatch=reg.search(line)
        if regMatch:
            #if regMatch.group(1).strip().startswith('t1'):
                #out_dict[regMatch.group(1)]=regMatch.group(2)
            out_dict[regMatch.group(1)]=(regMatch.group(2),regMatch.group(5))
    return out_dict


p=reg_match_int('showInterface.txt')
print "Dict:",p
print '-'*50
print " Interface Details"
print '-'*50
print ' Int Details    Status'
print '-'*50
for k,v in p.items():
    #if k.startswith('t1'):
    print '%s    %s  %s'%(k,v[0],v[1])

print '-'*50
