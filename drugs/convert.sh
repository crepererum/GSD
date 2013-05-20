#!/bin/bash

# config
input=$1
output=$2
datadir=$(mktemp -d)

for f in $input/*.zip; do
	tmpdir1=$(mktemp -d)
	unzip -q $f -d $tmpdir1
	for g in $tmpdir1/otc/*.zip; do
		tmpdir2=$(mktemp -d)
		unzip -q $g -d $tmpdir2
		for h in $tmpdir2/*.xml; do
			name=$(basename -s ".xml" $h)
			echo "convert $name"
			xpath -e "//ingredientSubstance/name/text()" $h 2>/dev/null | recode html..utf8 | sort > $datadir/$name.txt
		done
		rm -rf $tmpdir2
	done
	rm -rf $tmpdir1
done

echo "Create index and write result..."
./dicthelper.py $datadir > $output

rm -rf $datadir

