#!/bin/bash

if​ [ $# -eq "2" ]; then
  DATE​ = $(date + '%Y-%m-%d_%H-%M-%S'​);
  NAME​ = "$1_$DATE";
  sudo fswebcam -r 640x480​ - D $2 -d /dev​/video0 -i 0 $NAME​.jpg;
  sudo mv $NAME​.jpg /mnt​/usb​/uwphotos​/$NAME​.jpg;
else
  echo "Usage: ./webcam.sh pictureName delay(sec)";
fi
