#!/bin/dash

#############
#
#
# Testing pushy-add on a removed file
# Author: Nas
#
############

trap 'rm $exp $actual rm -dr $temp_dir' INT TERM EXIT HUP QUIT


PATH=$PATH:$(pwd)

temp_dir=$(mktemp -d)

cd $temp_dir

exp=$(mktemp)
actual=$(mktemp)


pushy-init 2>&1 "$actual"

cat > "$exp"<<HERE
	"Initialised empty repository in .pushy"
HERE

if ! diff "$exp" "$actual"
then
	echo "failed test"
	exit 1	
fi


echo "abc" > a
pushy-add 2>&1 "$actual"
pushy-commit 2>&1 "$actual"

rm a

pushy-add 2>&1 "$actual"
pushy-commit 2>&1 "$actual"


pushy-show 1:a 2>&1 "$actual"



echo "Passed! :)"

