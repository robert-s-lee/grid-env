#!/usr/bin/env python

import sys
import os
import subprocess
import pkg_resources
import time

# args
print("Arguments:")
print(f'Number of arguments: {len(sys.argv)} arguments.')
print(f'Argument List: {str(sys.argv)}')

# current wd
print("\nWorking Directory:")
print(f'os.getcwd={os.getcwd()}')

# python packages
print("\nPython Version:")
print(sys.version)

os.system("mkdir -p logs")

# network
print("\nNetwork:")
os.system("ip link show > ./logs/iplink.txt 2>&1")
os.system("ip route list > ./logs/iproute.txt 2>&1")

# what are mounted
print("\nFile Systems Mounted:")
os.system("df -kH > ./logs/df.txt 2>&1")

# files in current dir
print("\nFiles:")
os.system("find . -print > ./logs/find.txt 2>&1")

# conda
print("\nConda:")
os.system("conda env list > ./logs/conda.env.list.txt 2>&1")

print("\nPython Packages:")
os.system("pip freeze > ./logs/pip.freeze.txt 2>&1")

# libaries
print("\nLibraries")
os.system("ldconfig -p > ./logs/ldconfig.txt 2>&1")

# wait at least one minute
time.sleep(60) 
