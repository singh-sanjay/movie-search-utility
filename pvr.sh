#! /bin/sh

isBaahubaliInTheaters=`python ~/minionTheThird/workspace/bookmyshow/in_pvr.py`

if [ "$isBaahubaliInTheaters" = "True" ] ; then
    mpg123 -q -l 0 ~/Downloads/deadpool.mp3 &
fi

