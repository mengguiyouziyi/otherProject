#!/bin/bash
. /etc/profile
. ~/.bash_profile
export PYENV_VIRTUALENV_DISABLE_PROMPT=1
eval "$(pyenv init -)"
pyenv deactivate
pyenv activate env354
cd /data1/spider/menggui/otherProject/dim/extract_last/main/
tab_out="tyc_jichu_quan"
# 脚本获取第二个参数作为start
nohup python extract.py ${tab_out} intro $(cat intro.txt) >> intro.out 2>&1 &
