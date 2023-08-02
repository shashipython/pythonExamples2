import os
path='E:\pythonExamles\inPut2.txt'
fd=os.open(path,os.O_APPEND)
os.close(fd)
dst='E:\pythonExamles\hello.py'
os.link(path,dst)
