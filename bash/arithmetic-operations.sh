#!/bin/bash

read expr

echo $(echo "scale=10; $expr" | bc | xargs printf %.3f)