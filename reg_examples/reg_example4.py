import re

text = '10/02/1980  kdahfskjafd jhLFK 12/03/2016  fdskjhfdsa 7/2/30009'

pat = '\d{1,2}/\d{1,2}/\d{2,4}\s+'
print  re.findall(pat, text)
for match in re.findall(pat, text):
    print 'Found "%s"' % match