#!/bin/sh

# for zid in $zids  # where zids=z5423 zXXXX zYYYY ZAAAA
# do

# done

mlalias cs2041.wed17-strings |
grep -E '^\s*z[0-9]{7}' |
sed -E 's/\s*//g' |
sed -E 's/@.*//' | head -n 6 | 
while read zid
do
    ./acc.sh $zid
    # acc "$zid" |
    # sed -E -n '/^\s*User classes/,/^\s*Misc/p' |
    # head -n -1 |
    # tr ',' '\n' |
    # sed -E 's/^[^:]*://' |
    # grep -E '[A-Z]{4}[0-9]{4}t[0-3]_Student' |
    # sed -E 's/([A-Z]{4}[0-9]{4}).*/\1/'
done |
sort | uniq -c | sed -E 's/^\s*//' | sort -nr