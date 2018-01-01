#!/bin/bash

getFname () {
  num=$(($1 + 1))
  fname="ppm24bit bmp24bit ppm16 ppm256"
  echo $fname | cut -f$num -d' '
}

mkdir out

for i in {0..3}
do
  php common2.svg $i > file$i.svg
  mv file$i.svg out/$(getFname $i).svg
done

