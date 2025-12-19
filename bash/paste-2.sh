#!/bin/bash

paste -d';;\n' -s

## Much more long-winded way:
# rm -f splitme
# while IFS= read -r LINE; do
#   echo "$LINE" >> splitme
# done < /dev/stdin
# split -l 3 splitme split_
# paste -d';' -s split_*