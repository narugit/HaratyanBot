#!/bin/sh

#Debian用
working_directory=$(cd $(dirname $0)/..;pwd)
haratyan_url=`cat ${working_directory}/url.lock`
wget ${haratyan_url} -O ${working_directory}/haratyan.html
nkf -w --overwrite ${working_directory}/haratyan.html
python ${working_directory}/main.py
${working_directory}/shell/Scheduler.sh
