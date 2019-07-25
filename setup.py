from setuptools import find_packages, setup
import six


install_requires = []
for s in open('requirements.txt').readlines():
    if not s.startswith('#'):
        s = s.strip()
        lower_s = s.lower()
        install_requires.append(
            'Django >= 1.11.22, < 2'   # last 1.x ver compat w/ Py2
            if lower_s.startswith('django >=')
            else ('Django-AutoComplete-Light >= 3.2.10, < 3.3'   # last 3.2.x ver compat w/ Py2
                  if six.PY2 and lower_s.startswith('django-autocomplete-light')
                  else ('DjangoRESTFramework-Filters >= 0.10.2, < 1'   # last 0.x ver compat w/ Py2
                        if six.PY2 and lower_s.startswith('djangorestframework-filters')
                        else ('DjangoRESTFramework >= 3.9.4'   # last 0.x ver compat w/ Py2
                              if six.PY2 and lower_s.startswith('djangorestframework')
                              else ('Django-Filter >= 1.1.0, < 2'   # last 1.x ver compat w/ Py2
                                    if six.PY2 and lower_s.startswith('django-filter')
                                    else s)))))


setup(
    name='Arimo-IoT-DataAdmin',
    author='Arimo',
    author_email='DSAR@Arimo.com',
    url='https://github.com/adatao/IoT-DataAdmin',
    version='0.0.0',
    description='Arimo IoT Data Admin',
    long_description='Arimo IoT Data Admin',
    keywords='Arimo IoT Data Admin',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires)
