#!/bin/sh

for name in {cg,marmot,wombat,swiss}
do
  for i in $(seq 10 20 90|tac)
  do
    echo -n " ${name}${i}     : "
    compare -metric PSNR ${name}.bmp out/${name}${i}.jpg diff.jpg
    echo
  done
done

