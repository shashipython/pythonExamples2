

import os
import stat
path="E:\pythonExamles\inPut2.txt"

print "==>",os.access(path,os.R_OK)

print "Write Mode only:",os.chmod(path,stat.S_IREAD)


print "==>",os.access(path,os.R_OK)
print "==>",os.access(path,os.W_OK)

print "Write Mode only:",os.chmod(path,stat.S_IWRITE)
print "==>",os.access(path,os.W_OK)


print "getcwdu:",os.getcwdu(),os.getcwd()