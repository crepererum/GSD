#!/usr/bin/env python3

import argparse

# parse command line arguments
parser = argparse.ArgumentParser(description="Cleans the data from unknown values")
parser.add_argument("--input", type=open, required=True, help="Input SSV file")
parser.add_argument("--output", type=argparse.FileType("a"), required=True, help="Output SSV file")
parser.add_argument("--columnList", type=argparse.FileType("a"), required=True, help="Output list of removed columns")
parser.add_argument("--rowList", type=argparse.FileType("a"), required=True, help="Output list of dropped rows")
parser.add_argument("--threshold", type=float, required=True, help="Threshold of rate of unknown values to delete a column")

args = parser.parse_args()

# detect number of unknown values
print("Read file...", end="")
total = 0
counts = []
for line in args.input:
	column = 0
	for cell in line.split(" "):
		valid = True
		try:
			test = float(cell)
		except ValueError:
			valid = False

		if total == 0:
			counts.append(0)

		if not valid:
			counts[column] += 1

		column += 1

	total += 1
print("ok (%i rows)" % total)

# check for columns to remove
print("Find columns that should be removed...", end="")
remove = []
idx = 0
nRemoved = 0
for x in counts:
	if x >= args.threshold * total:
		args.columnList.write("%i\n" % idx)
		remove.append(True)
		nRemoved += 1
	else:
		remove.append(False)
	idx += 1
print("ok (%i columns removed)" % nRemoved)

# write output
print("Write output and drop rows...", end="")
args.input.seek(0)
idx = 0
nDropped = 0
for line in args.input:
	result = []
	column = 0
	valid = True
	for cell in line.split(" "):
		if not remove[column]:
			try:
				test = float(cell)
				result.append(cell.rstrip())
			except ValueError:
				valid = False
				break
		column += 1

	if valid:
		args.output.write("%s\n" % " ".join(result))
	else:
		nDropped += 1
		args.rowList.write("%i\n" % idx)

	idx += 1
print("ok (%i rows dropped)" % nDropped)

# clean up
args.input.close()
args.output.close()
args.columnList.close()
args.rowList.close()

