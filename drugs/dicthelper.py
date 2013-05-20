#!/usr/bin/env python

import os
import sys

dir = sys.argv[1]
all = set()

for f in os.listdir(dir):
	for l in open(dir + "/" + f).readlines():
		all.add(l.strip())

all = sorted(all)

for f in os.listdir(dir):
	this = set()
	for l in open(dir + "/" + f).readlines():
		this.add(l.strip())
	first = True
	for x in all:
		if first:
			first = False
		else:
			sys.stdout.write(" ")
		if x in this:
			sys.stdout.write("1")
		else:
			sys.stdout.write("0")
	sys.stdout.write("\n")

