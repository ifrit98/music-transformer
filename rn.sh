#!/bin/sh

counter=0
TMP=/tmp/copyNoStructure

rm -rf $TMP
mkdir $TMP 

cp -r . $TMP 
find $TMP -type f  | \
while read f 
do 
	rm -f "$f"
done 


#grep -v $0
find . -type f     | \
while read f 
do 
	# echo $counter 
	counter=`echo $counter + 1 | bc`
	dir=`dirname "$f"`
	cp "$f" "$TMP/$counter.midi"
done 

echo ======
find .
echo ======
find $TMP 
echo =====
