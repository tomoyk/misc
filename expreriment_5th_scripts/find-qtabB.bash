#!/bin/bash

for i in {2..64}
do
  cjpeg -qtables qtabB$i marmot.bmp > marmotB.jpg
  echo -n "qtabB$i: "
  wc -c marmotB.jpg | cut -f1 -d ' '
done
