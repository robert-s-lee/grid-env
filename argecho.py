import sys
import os
from kubernetes import client, config

print(f'Number of arguments: {len(sys.argv)} arguments.')
print(f'Argument List: {str(sys.argv)}')
print(f'os.getcwd={os.getcwd()}')
