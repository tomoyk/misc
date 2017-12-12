#!/bin/bash

echo -e "FileName    \t$(seq 10 20 90 | tr '\n' ' ' | sed 's/ /    /g')"

for base in {cg,marmot,wombat,swiss}
do
  echo -en "${base}:  "
  if [ $(echo $base | wc -c) -lt 4 ]
  then
    echo -n "    "
  fi
  echo -en "\t"

  # getSize
  baseSize=$(wc -c ${base}.bmp | cut -f1 -d ' ')

  for i in $(seq 10 20 90)
  do
    echo "$(wc -c out/${base}${i}.jpg | cut -f1 -d ' ' | tr -d '\n') / $baseSize * 100" | bc -l | cut -c1-5 | tr '\n' ' '
  done
  echo
done
