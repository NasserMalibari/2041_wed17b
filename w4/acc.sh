#!/bin/dash

acc $1 |
sed -E -n '/^\s*User classes/,/^\s*Misc/p' |
head -n -1 |
tr ',' '\n' |
sed -E 's/^[^:]*://' |
grep -E '[A-Z]{4}[0-9]{4}t[0-3]_Student' |
sed -E 's/([A-Z]{4}[0-9]{4}).*/\1/'

