#!/bin/bash

awk 'BEGIN { ORS=OFS="" }
    { 
        if ( FNR % 2 == 0 ){ print $0, "\n" } 
        else { print $0, ";" }
    }'