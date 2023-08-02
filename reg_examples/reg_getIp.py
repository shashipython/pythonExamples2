import re
reg_cobj=re.compile("(\d+\.\d+\.\d+\.\d+).*")

fd=open('showInt','r')
for line in fd.readlines():
    p=reg_cobj.search(line)
    if p:
        print p.group(1)

fd.close()