#!/bin/bash

countries=(`cat`)
echo "${countries[@]/[A-Z]/.}"