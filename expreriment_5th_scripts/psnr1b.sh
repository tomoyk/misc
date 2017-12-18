#!/bin/sh

for name in {cg,marmot,wombat,swiss}
do
  for i in $(seq 10 20 90|tac)
  do
    echo -n " ${name}${i}     : "
    display out/${name}${i}.jpg
    echo
  done
done

