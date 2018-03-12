#!/bin/sh

#Debian用
working_directory=`dirname $0`
haratyan_url=`cat ${working_directory}/url.lock`
wget ${haratyan_url} -O haratyan.html
nkf -w --overwrite haratyan.html
python ${working_directory}/main.py
rm ${working_directory}/haratyan.html
${working_directory}/Scheduler.sh
