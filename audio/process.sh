#!/usr/bin/env bash

# config
tmpdir=$(mktemp -d)

length=$(($#))
for iname in "${@:2:$length}"; do
	bname=$(basename "$iname")
	oname="$tmpdir/$bname.wav"
	echo "Convert to wav: \"$iname\""
	sox --norm "$iname" "$oname"
done;

echo "Analyze..."
./analyze.jl $tmpdir/*.wav > $1

echo "Cleanup..."
rm -rf $tmpdir


