#!/bin/bash

read n
read -r -a A
declare -A occurs
for i in ${A[@]}; do
    if [[ ${occurs[$i]+_} ]]; then
    # if [[ -v occurs[$i] ]]; then # in Bash 4.3+ this is equivalent to line above
        occurs[$i]=2
    else
        occurs[$i]=1
    fi
done
for k in ${!occurs[@]}; do
    if [[ ${occurs[$k]} == 1 ]]; then
        echo $k
    fi
done