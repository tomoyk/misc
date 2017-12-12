#!/bin/bash

mkdir out/

echo -e "FileName    \t$(seq 10 20 90 | tr '\n' ' ' | sed 's/ /    /g')"

for base in {cg,marmot,wombat,swiss}
do
  echo -en "${base}:  "
  if [ $(echo $base | wc -c) -lt 4 ]
  then
    echo -n "    "
  fi
  echo -en "\t"
  for i in $(seq 10 20 90)
  do
    wc -c out/${base}${i}.jpg | cut -f1 -d ' ' | tr '\n' ' '
  done
  echo
done
