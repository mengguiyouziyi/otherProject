#!/bin/bash
. /etc/profile
. ~/.bash_profile
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init -)"
pyenv deactivate
pyenv activate env354
cd /data1/spider/menggui/otherProject/dim/extract_last/main/
# 这是传给extract.py文件的三个参数，分别是 查询表、抽取类别、游标开始数字
tab_out="tyc_jichu_quan"
in_cat="contactinfo"
start_num=$(cat contactinfo.txt)
nohup python extract.py ${tab_out} ${in_cat} ${start_num} >> ${in_cat}.out 2>&1 &

