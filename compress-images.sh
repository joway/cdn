# /bin/bash

source=$1
convert -resize 2073600@ $source $source
width=`identify -format %w $source`
height=`identify -format %h $source`
convert -strip -interlace Plane -quality 70% "$source"  "$source"
echo "$source finished!"
