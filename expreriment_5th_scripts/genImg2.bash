#!/bin/bash

for i in {32,64,96,128}
do
  cjpeg -qtables qtab${i} marmot.bmp > marmot${i}.jpg
done

wc -c marmot*
