#!/usr/bin/env sh

fileIn="$3"
fileOut="$4"
end="$2"
delta=$(expr "$end" "-" "$1" "+" "1")

head -n"$end" "$fileIn" | tail -n"$delta" >"$fileOut"

