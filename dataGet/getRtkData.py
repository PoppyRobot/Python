#!/usr/bin/python
# -*- coding: utf-8 -*-

# 从原始eRTK日志中获取载波和伪距测量值
import os
import sys
import shutil

FileName="RtkData.txt"

if len(sys.argv) < 3:
	print 'Usage:', sys.argv[0], "FileName"+" FolderName"
	exit(1)

	
for i in range(1, len(sys.argv)):
	print "Pram", i, sys.argv[i]
	
#os.system(CMD)
# 删除前50行数据
#CMD="sed '1,120d' %s > file.copy" % FileName
#print CMD
#os.system(CMD)

#CMD="mv file.copy %s" % FileName
#print CMD
#os.system(CMD)

for prn in range(2, 33):
	#CMD = "grep 'sendrtcmobs: ant_id=0 PRN=%-2d' %s | awk '{print $6,$7,\"     \",$8,$9}' > PRN_%d.txt" % (prn, FileName, prn)
	CMD = "grep 'sat=%-2d rcv=1' %s | awk '{print $3,$5,$6,\"     \",$7,$8}' > R_%d.txt" % (prn, FileName, prn)
	print CMD
	os.system(CMD)
	
for prn in range(2, 33):
	#CMD = "grep 'sendrtcmobs: ant_id=0 PRN=%-2d' %s | awk '{print $6,$7,\"     \",$8,$9}' > PRN_%d.txt" % (prn, FileName, prn)
	CMD = "grep 'sat=%-2d rcv=2' %s | awk '{print $3,$5,$6,\"      \",$7,$8}' > B_%d.txt" % (prn, FileName, prn)
	print CMD
	os.system(CMD)
	
#替换载波和伪距的标识字段 P[0]= P[0]=  L[0]= L[0]=
CMD1 = "ls *.txt | xargs sed -i \"s/P://g\""
print CMD1
os.system(CMD1)

CMD2 = "ls *.txt | xargs sed -i \"s/L://g\""
print CMD2
os.system(CMD2)

CMD3 = "ls *.txt | xargs sed -i \"s/0.000000       /0.000000              /g\""
print CMD3
os.system(CMD3)

CMD4 = "ls *.txt | xargs sed -i \"s/t.time=//g\""
print CMD4
os.system(CMD4)

print 'Delete file size=0'
for f in os.listdir("."):
	fsize = os.stat(f)
	if fsize.st_size == 0L:
		#print f, fsize.st_size
		os.remove(f)
		
#移动文件到指定目录		
FolderName = sys.argv[2]
DEL_CMD = "rm %s -rf" % FolderName
os.system(DEL_CMD)
print DEL_CMD

isExists = os.path.exists(FolderName)
if not isExists:
	os.mkdir(FolderName)

for prn in range(2, 33):
	FileNameR = "R_%d.txt" % (prn)
	isExistsR = os.path.exists(FileNameR)
	if isExistsR:
		shutil.move(FileNameR, FolderName)
		print 'move %s to %s' % (FileNameR, FolderName)
		
	FileNameB = "B_%d.txt" % (prn)
	isExistsB = os.path.exists(FileNameB)
	if isExistsB:
		shutil.move(FileNameB, FolderName)
		print 'move %s to %s' % (FileNameB, FolderName)




