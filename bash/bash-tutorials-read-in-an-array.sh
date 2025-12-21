#!/bin/bash

countries=()
while IFS= read line; do
    countries+=($line)
done < /dev/stdin
echo "${countries[@]}"