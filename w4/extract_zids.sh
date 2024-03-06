#!/bin/dash

mlalias cs2041.wed17-strings |
grep -E '^\s*z[0-9]{7}' |
sed -E 's/\s*//g' |
sed -E 's/@.*//'