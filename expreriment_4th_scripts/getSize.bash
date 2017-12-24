#!/bin/bash

getSize(){
  echo -ne "${1}  "
  if [ $(echo $1|wc -c) -lt 4 ]; then
    echo -n "    "
  fi
  echo -ne "\t"
  for ext in {bmp,ppm,png}
  do
    wc -c ${1}.${ext} | awk '{print $1}' | tr '\n' ' '
  done
  echo 
}

echo -e "FileName    \tBMP    PPM    PNG"
getSize marmot
getSize cg
getSize lattice1

