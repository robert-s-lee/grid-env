import sys
import os
from kubernetes import client, config
import pkg_resources

# a simple script to echo arguments and dump out K8s environment
# https://github.com/kubernetes-client/python

# args
print(f'Number of arguments: {len(sys.argv)} arguments.')
print(f'Argument List: {str(sys.argv)}')

# current wd
print(f'os.getcwd={os.getcwd()}')

# python packages
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
print(installed_packages_list)
