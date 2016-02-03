#!/usr/bin/python
# -*- coding: utf-8 -*-

# 从原始eRTK日志中获取载波和伪距测量值
import os
import sys
import shutil

FileName=sys.argv[1]

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

for prn in range(1, 33):
	#CMD = "grep 'sendrtcmobs: ant_id=0 PRN=%-2d' %s | awk '{print $6,$7,\"     \",$8,$9}' > PRN_%d.txt" % (prn, FileName, prn)
	CMD = "grep 'CoarsedpCheck: COARSE_DPLER:%-2d' %s | awk '{print $5, $6, $7, $8, $9}' > R_%d.txt" % (prn, FileName, prn)
	# CoarsedpCheck: COARSE_DPLER:8 
	print CMD
	os.system(CMD)

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




