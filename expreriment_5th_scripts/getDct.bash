#!/bin/bash

#
# gcc DCT2.c -lm -o dct2
#

for file in $(ls 8x8*.pgm)
do
  echo -ne "$file  \t"
  ./dct2 $file
done
