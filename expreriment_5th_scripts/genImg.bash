#!/bin/bash

for base in {cg,marmot,wombat,swiss}
do
  for i in $(seq 10 20 90)
  do
    cjpeg -quality $i ${base}.bmp > out/${base}${i}.jpg
  done
done
