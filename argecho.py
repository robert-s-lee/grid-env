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

# what are mounted
print("\nFile Systems Mounted:")
os.system("mkdir -p logs")
os.system("df -kH | tee ./logs/df.txt")

# python packages
print("\nPython Version:")
print(sys.version)

# files in current dir
print("\nFiles:")
os.system("find . -print | tee ./logs/find.txt")

# files in current dir
print("\nConda:")
os.system("conda env list | tee ./logs/conda.env.list.txt")

print("\nPython Packages:")
os.system("pip freeze | tee ./logs/pip.freeze.txt")
  