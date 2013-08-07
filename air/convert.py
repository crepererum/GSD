#!/usr/bin/env python

import sys

# parse args
fnameIn = sys.argv[1]
fnameOut = sys.argv[2]
fnameColumns = sys.argv[3]

# data structures
skip = -2
map = {}
positions = set()
timestamps = set()

# read data
fIn = open(fnameIn)
for l in fIn:
	if skip < 0:
		skip += 1
	else:
		raw = l.split("|")
		if len(raw) == 28:
				state = raw[2]
				county = raw[3]
				site = raw[4]
				date = raw[10]
				time = raw[11]
				valueRaw = raw[12]

				pos = "%s.%s.%s" % (state, county, site)
				positions.add(pos)

				if len(valueRaw) > 0:
					timestamp = date + time
					timestamps.add(timestamp)
					if not timestamp in map:
						map[timestamp] = {}
					map[timestamp][pos] = valueRaw

fIn.close()

# prepare output
positions = sorted(positions)
timestamps = sorted(timestamps)

# output column list
columns = open(fnameColumns, "w")
for pos in positions:
	columns.write(pos)
	columns.write("\n")
columns.close()

# output
out = open(fnameOut, "w")
for timestamp in timestamps:
	# print only timestamps with enough data
	if len(map[timestamp]) >= 0.75 * len(positions):
		avg = 0.0
		for pos in map[timestamp]:
			avg += float(map[timestamp][pos])
		avg /= len(map[timestamp])
		avg = str(avg)

		first = True
		for pos in positions:
			if first:
				first = False
			else:
				out.write(" ")
			if pos in map[timestamp]:
				out.write(map[timestamp][pos])
			else:
				out.write(avg)
		out.write("\n")
out.close()

