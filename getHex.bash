#!/bin/bash

getChar(){
  # getChar $hex $startField $endField $lineNumber
  result=`echo ${1} | tr ',' '\n' | cut -d ' ' -f${2}-${3} | head -${4} | tail -1`
  echo $result | tr -d '\n'
  echo -en '  \t'
  echo $result | awk '{print $4$3$2$1}' | tr [a-z] [A-Z] | sed 's/.*/ibase=16; &/g' | bc
}

for i in $(ls *.bmp)
do
  hex=`od -tx1 $i | head -5 | cut -d ' ' -f2- | tr '\n' ','`

  ### Get hex-bytes
  echo "========== $i =========="
  echo -n "FileSize: "
  getChar "$hex" 3 6 1
  echo -n "   Width: "
  getChar "$hex" 3 6 2
  echo -n "  Height: "
  getChar "$hex" 7 10 2
  echo -n "ColorBit: "
  getChar "$hex" 13 14 2
  echo -n "DataSize: "
  getChar "$hex" 3 6 3

  ### Delimiter
  yes + | head -50 | tr -d '\n'
  echo
done

