#!/bin/bash
#$1 is process name

sed 1d ./trace.result | awk '{print $7, $11, $15}' > ./tmp.txt
mv ./tmp.txt ./trace.result

