#!/bin/bash

awk '{ if ($2 >= 50 && $3 >= 50 && $4 >= 50){result = "Pass"} else {result = "Fail"} print $1, ":", result }'