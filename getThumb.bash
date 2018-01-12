#!/bin/bash -eu

# FILENAME="Eject.mp4"
# IMAGENAME="out2.jpg"
FILEPATH="$PWD"

if [ -v "$1" ] || [ -v "$2" ] ; then
  echo "Usage: CMD [SourceVideo] [ThumbnailFile]"
  exit 1
else
  FILENAME="$1"
  IMAGENAME="$2"
fi

sudo docker run --rm -v ${FILEPATH}:/tmp jrottenberg/ffmpeg -stats -i /tmp/${FILENAME} -y -vframes 1 -f image2 -ss 00:00:05 /tmp/${IMAGENAME}

exit 0
