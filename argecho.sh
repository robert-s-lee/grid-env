#!/usr/bin/env bash

# args
echo "Arguments:"
echo "$@" > ./logs/args.txt

# current wd
echo "Working Directory:"
pwd > ./logs/pwd.txt

# python packages
echo "Python Version:"
python --version > ./logs/pythonversion.txt

mkdir -p logs

# network
echo "Network:"
ifconfig -a > ./logs/ifconfig.txt

# what are mounted
echo "File Systems Mounted:"
df -kH > ./logs/df.txt

# files in current dir
echo "Files:"
find . -print > ./logs/find.txt

# conda
echo "Conda:"
conda env list > ./logs/conda.env.list.txt

# python
echo "Python Packages:"
pip freeze > ./logs/pip.freeze.txt
  