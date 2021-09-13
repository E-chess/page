import os
import pkg_resources

installed_packages = pkg_resources.working_set
installed_packages_dict = {}
for i in installed_packages:
    installed_packages_dict[i.key] = i.version

poetry_value = installed_packages_dict.get('poetry')
if poetry_value != '1.1.2':
    os.system('pip install poetry==1.1.8')

os.system('python page.py')
