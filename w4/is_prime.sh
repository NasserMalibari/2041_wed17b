#!/bin/dash

if [ "$#" -ne 1 ]
then
    echo "Usage: ./is_prime <num>"
    exit 2
fi

#TODO: check $1 is a number

# main
num=$1
i=2

# i < sqrt(n)
# i * i < n
while [ $(( i * i)) -lt $num ]
do

    # if num % i == 0 
    rem=$((num % i))
    if [ $rem -eq 0 ]
    then
        echo "$num is not prime"
        exit 1
    fi

    i=$(( i+1 ))
done

echo "$num is prime"
exit 0
