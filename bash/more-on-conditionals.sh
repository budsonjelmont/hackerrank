#!/bin/bash

read A
read B
read C

if [[ $A -eq $B && $B -eq $C && $A -eq $C  ]]
then
    echo "EQUILATERAL"
elif [[ ( $A -eq $B ) || ( $A -eq $C ) || ( $B -eq $C )  ]]
then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi