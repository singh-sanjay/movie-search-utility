#! /bin/sh

isBaahubaliInPVR=`python ~/minionTheThird/workspace/bookmyshow/isBaahubaliInPVR.py`

if [ "$isBaahubaliInPVR" = "True" ] ; then
    mpg123 -q -l 0 ~/Downloads/deadpool.mp3 &
fi

# cant send email from local network, set up mail functionality on other system
