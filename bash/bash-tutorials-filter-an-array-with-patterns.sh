#!/bin/bash

countries=()
pattern="[aA]"
while IFS= read country; do
    if [[ ! $country =~ $pattern ]];
    then
        countries+=($country)
    fi
done < /dev/stdin
echo "${countries[@]}"