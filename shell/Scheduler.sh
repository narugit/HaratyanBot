#!/bin/sh

working_directory=`dirname $0`

set_new() {
  at 17:00 tomorrow -f ${working_directory}/HaratyanCheck.sh
}

set_old() {
  at now +10minutes -f ${working_directory}/HaratyanCheck.sh
}

isNew=`sed -n 1p ${working_directory}/log.txt`

if [ ${isNew} = New ]; then
  set_new
else
  set_old
fi
