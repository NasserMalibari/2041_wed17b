#!/bin/sh

if [ $# -eq 1   ]
then
    end=$1
    start=1
    increment=1
elif [ $# -eq 2 ]
then
    start="$1"
    end="$2"
    increment=1
elif [ $# -eq 3 ]
then
    start="$1"
    end="$3"
    increment="$2"
else 
    echo "Wrong number of args!" >&2  # note >&2 sends to stderr
    exit 1
fi

if [ "$start" -eq "$start" ] 2> /dev/null
then
    :
else
    echo "not a number!"
    exit 1
fi

if [ "$end" -eq "$end" ] 2> /dev/null
then
    :
else
    echo "not a number!"
    exit 1
fi

if [ "$increment" -eq "$increment" ] 2> /dev/null
then
    :
else
    echo "not a number!"
    exit 1
fi


#current = start
current="$start"

# while current <= end
while test $current -le $end
do

    # print current
    echo "$current"
    # increment
    current=$(( current + increment  ))

done


