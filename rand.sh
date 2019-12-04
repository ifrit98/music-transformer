#!/bin/sh

MAXCOUNT=100
MAXVAL=99999
count=1

echo
echo "$MAXCOUNT random numbers:"
echo "[(rand + rand) x rand] / prime"
echo "-----------------"
while [ "$count" -le $MAXCOUNT ]      # Generate 10 ($MAXCOUNT) random integers.
do
  rand=$RANDOM 
  rand1=$RANDOM
  rand2=$RANDOM

  let "rand3 = $RANDOM % $MAXVAL"
  let "fn = (rand + rand1) * rand3 - 17 * $rand3"

  echo [[$rand + $rand1] x $rand2 - [17 x $rand3]] = $fn
  let "count += 1" 
done
echo "-----------------"
