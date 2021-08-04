#!/usr/bin/env python

import sys
import os
import subprocess
import pkg_resources

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
os.system("ifconfig -a | tee ./logs/ifconfig.txt")

# what are mounted
print("\nFile Systems Mounted:")
os.system("df -kH | tee ./logs/df.txt")

# files in current dir
print("\nFiles:")
os.system("find . -print | tee ./logs/find.txt")

# conda
print("\nConda:")
os.system("conda env list | tee ./logs/conda.env.list.txt")

print("\nPython Packages:")
os.system("pip freeze | tee ./logs/pip.freeze.txt")
  