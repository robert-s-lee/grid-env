import sys
import pkg_resources

# python packages
print("\nPython Version:")
print(sys.version)

print("\nPython Packages:")
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
   for i in installed_packages])
for p in installed_packages_list:
    print(p)
