#!/bin/sh

working_directory=$(cd $(dirname $0)/..;pwd)

set_new() {
  at 17:00 tomorrow -f ${working_directory}/shell/HaratyanCheck.sh
}

set_old() {
  at now +10minutes -f ${working_directory}/shell/HaratyanCheck.sh
}

isNew=`sed -n 1p ${working_directory}/log.txt`

if [ ${isNew} = New ]; then
  set_new
else
  set_old
fi
