#!/usr/bin/env python3

import argparse

# parse command line arguments
parser = argparse.ArgumentParser(description="Sums up columns and sort them by sum")
parser.add_argument("--input", type=open, required=True, help="Input SSV file")
parser.add_argument("--output", type=argparse.FileType("a"), required=True, help="Sorted list with two columns (index and sum)")

args = parser.parse_args()

# read input file
sums = []
first = True
for line in args.input:
	raw = line.split(" ")
	data = list(map(lambda s: int(s), raw))
	if first:
		sums = data
		first = False
	else:
		sums = list(map(lambda x,y: x + y, sums, data))

# sort
sums = sorted(enumerate(sums), key=lambda z: z[1], reverse=True)

# write output
for s in sums:
	args.output.write("%i %i\n" % s)

# clean up
args.input.close()
args.output.close()

