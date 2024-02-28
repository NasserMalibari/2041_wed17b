#!/bin/sh

for file in *.c # for file in a.c b.c uniq.c wc.c
do
    echo "$file includes:"
    
    grep -E '^\s*#include' "$file" | 
    sed -E 's/^\s*#include\s*[<"]/\t/'  | # remove everything before source file name
    sed -E 's/[>"].*//'  # remove the last bit 
done