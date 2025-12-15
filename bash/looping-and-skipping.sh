#!/usr/bin/bash
# https://www.hackerrank.com/challenges/bash-tutorials---looping-and-skipping/problem?isFullScreen=true
for i in $(seq 1 100); do
  if [ "$(( $i % 2 ))" -ne "0" ]; then
    echo $i;
  fi;
done