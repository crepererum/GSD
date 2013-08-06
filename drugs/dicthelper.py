#!/usr/bin/env python

import os
import sys

dir = sys.argv[1]
output = open(sys.argv[2], "w")
all = set()

# build list of all possible parts
for f in os.listdir(dir):
	tmp = open(dir + "/" + f)
	lines = tmp.readlines()
	tmp.close()
	for l in lines:
		all.add(l.strip().lower())

# sort them and output columns
all = sorted(all)
for x in all:
	print(x)

# lookup all drugs and write binary vectors
for f in os.listdir(dir):
	this = set()
	for l in open(dir + "/" + f).readlines():
		this.add(l.strip().lower())

	first = True
	for x in all:
		if first:
			first = False
		else:
			output.write(" ")

		if x in this:
			output.write("1")
		else:
			output.write("0")

	output.write("\n")

# clean up
output.close()

