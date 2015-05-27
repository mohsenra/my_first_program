#!/usr/bin/python3

fh = open ("gigbang.srt")
o=0
for lin in fh.readlines():
	print(o,lin,end='')
	o=o+1
