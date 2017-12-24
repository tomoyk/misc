#!/bin/bash

s=$((320*240))

echo -e "Fname  \t\t\tSize\tN\tColor"
for file in $(ls *.bmp)
do
  d=`wc -c $file | cut -d ' ' -f1`
  N=$(($d * 8 / $s))
  col=$((2 ** $N))
  echo -e "$file:  \t$d \t$N \t$col"
done
