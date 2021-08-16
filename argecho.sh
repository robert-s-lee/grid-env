#!/usr/bin/env bash

mkdir -p logs

# args
echo "Arguments:"
echo "$@" > ./logs/args.txt 2>&1

# current wd
echo "Working Directory:"
pwd > ./logs/pwd.txt 2>&1

# python packages
echo "Python Version:"
python --version > ./logs/pythonversion.txt 2>&1

# network
echo "Network:"
ip link show > ./logs/iplink.txt 2>&1
ip route list > ./logs/iproute.txt 2>&1

# what are mounted
echo "File Systems Mounted:"
df -kH > ./logs/df.txt 2>&1

# files in current dir
echo "Files:"
find . -print > ./logs/find.txt 2>&1

# conda
echo "Conda:"
conda env list > ./logs/conda.env.list.txt 2>&1

# python
echo "Python Packages:"
pip freeze > ./logs/pip.freeze.txt 2>&1

# libraries
echo "Libraries"
ldconfig -p > ./logs/ldconfig.txt 2>&1" 

# wait at least one minute
sleep 60