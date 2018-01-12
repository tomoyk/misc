#!/bin/bash -e

# FILENAME="Eject.mp4"
# IMAGENAME="out2.jpg"
FILEPATH="$PWD"
GETPOINT="00:00:10"

##
# Check parameters
##
if [ -v "$1" ] || [ -v "$2" ] ; then
  echo "Usage: CMD <SourceVideo> <ThumbnailFile> [getTime]"
  exit 1
fi

if [ ! -v $3 ] ; then
  GETPOINT="$3"
fi

##
# Does set file exist ?
##
if [ -f "$1" ] ; then
  FILENAME="$1"
  IMAGENAME="$2"
else
  echo "No such file ($1)"
  exit 1
fi

sudo docker run \ 
  --rm \
  -v ${FILEPATH}:/tmp \
  jrottenberg/ffmpeg \
  -ss ${GETPOINT} \
  -i /tmp/${FILENAME} \
  -y -vframes 1 \
  -f image2 \
  /tmp/${IMAGENAME}

exit 0
