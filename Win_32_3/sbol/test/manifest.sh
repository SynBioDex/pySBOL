#!/bin/bash

for directory in $(find * -maxdepth 0 -type d -print)
do
    cd $directory
    find * -not -name "manifest" -type f  -print > manifest
    cd ..
done
