#!/bin/bash
. /etc/profile
. ~/.bash_profile
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init -)"
pyenv deactivate
pyenv activate env354
cd /data1/spider/menggui/otherProject/dim/extract_last/main/
tab_out="tyc_core_team"
in_cat="teaminfo"
start_num=$(cat base.txt)
nohup python extract.py ${tab_out} ${in_cat} ${start_num} >> ${in_cat}.out 2>&1 &
