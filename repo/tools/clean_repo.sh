#! /usr/bin/zsh

for folder in $1/* ; do
    if [ -d $folder/build ] ; then
        echo "Cleaning" $folder
        rm build -rf $folder/build
    fi
done;