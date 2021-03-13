#!/bin/bash

read -erp "Title:" title;
filename=$(tr '[:upper:]' '[:lower:]' <<<"${title//[ ]/_}")
echo "$filename"
echo "---" > "$filename.markdown"
echo "title : \"$title\" " >> "$filename.markdown"
read -erp "Subtitle:" subtitle;
echo "subtitle : \"$subtitle\" " >> "$filename.markdown"
echo "date : `date +%FT%T%:z`" >> "$filename.markdown"
echo "---" >> "$filename.markdown"
mv "$filename.markdown" content/note/

$EDITOR content/note/"$filename.markdown"
