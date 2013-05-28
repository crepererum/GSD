#!/usr/bin/env sh

fileIn="$1"
fileOut="$2"
lineCount=$(wc -l "$fileIn" | sed -E "s/^([0-9]*).*/\\1/")
rangeWidth=$(python -c"import math;print(int(math.log10($lineCount))+1)")
nl -nrz -s" " -w"$rangeWidth" "$fileIn" | sed -E "s/^/0./g" >"$fileOut"

