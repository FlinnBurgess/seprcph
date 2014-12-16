#!/bin/bash
# This is the file used for builds on the Jenkins server.

PYENV_HOME=$WORKSPACE/.pyenv/

# Delete previously built virtualenv
if [ -d $PYENV_HOME ]; then
    rm -rf $PYENV_HOME
fi

# Create virtualenv and install necessary packages
virtualenv --system-site-packages $PYENV_HOME
. $PYENV_HOME/bin/activate

tree .

pip2.7 install --quiet pep8
pip2.7 install --quiet pylint
pip2.7 install --quiet $WORKSPACE/
pylint -f parseable -d C0301,R0903,C0103,C0330,R0913 seprcph/ | tee pylint.out
pep8 --ignore=E128,E501,E126 seprcph/ | tee pep8.out
python2.7 setup.py test
