#!/bin/sh
for i in {32,64,96,128}
do
  echo -n "marmot${i}  : "
  compare -metric PSNR marmot.bmp marmot${i}.jpg diff.jpg
  echo
done

