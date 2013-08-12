#!/usr/bin/env python3

import argparse
import sys

# parse command line arguments
parser = argparse.ArgumentParser(description="Removes lines by index")
parser.add_argument("--input", type=open, required=True, help="Input file from which lines get dropped")
parser.add_argument("--output", type=argparse.FileType("a"), required=True, help="Output data")
parser.add_argument("--rowList", type=open, required=True, help="List of row indices that should be dropped")

args = parser.parse_args()

# build filter
filter = set(map(lambda l: int(l.rstrip()), args.rowList.readlines()))

# process
idx = 0
for l in args.input:
	if not idx in filter:
		args.output.write("%s\n" % l.rstrip())
	idx += 1

# clean up
args.input.close()
args.output.close()
args.rowList.close()

