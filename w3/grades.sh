#!/bin/sh


while read id mark _restOfLine
do

    if [ $mark -lt 50 ]
    then
        echo "$id FL"
    else 
        echo "$id PS"
    fi

done