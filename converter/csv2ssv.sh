#!/usr/bin/env sh

cat "$1" | sed -E "s/, */ /g" > "$2"

