import sys
import os
import pkg_resources
import subprocess

# args
print("Arguments:")
print(f'Number of arguments: {len(sys.argv)} arguments.')
print(f'Argument List: {str(sys.argv)}')

# current wd
print("\nWorking Directory:")
print(f'os.getcwd={os.getcwd()}')

# what are mounted
print("\nFile Systems Mounted:")
result = subprocess.Popen(['df', '-kH'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
while(True):
   retcode = result.poll() 
   line = result.stdout.readline()
   print(line.decode("utf-8").strip())
   if retcode is not None:
      break

# python packages
print("\nPython Version:")
print(sys.version)

print("\nPython Packages:")
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
print(installed_packages_list)
