#!/bin/dash


i=2
num=$1

while [ $i -lt $num ]
do
    if ./is_prime.sh "$i" > /dev/null
    then
        echo "$i"
    fi

    i=$(( i + 1 ))
done

prog1 && prog2 && prog3