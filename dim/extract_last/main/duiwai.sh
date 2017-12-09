#!/bin/bash
. /etc/profile
. ~/.bash_profile
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init -)"
pyenv deactivate
pyenv activate env354
cd /data1/spider/menggui/otherProject/dim/extract_last/main/
tab_out="tyc_out_investment"
in_cat="duiwai"
start_num=$(cat duiwai.txt)
nohup python extract_no_name.py ${tab_out} ${in_cat} ${start_num} >> ${in_cat}.out 2>&1 &
