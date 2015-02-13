from setuptools import find_packages, setup
import os.path
import sys


def read_project_version(package):
    py = os.path.join(package, '__init__.py')
    __version__ = None
    for line in open(py).read().splitlines():
        if '__version__' in line:
            exec(line)
            break
    return __version__

NAME = 'confduino'
URL = 'https://github.com/ponty/confduino'
DESCRIPTION = 'Arduino software configurator'
VERSION = read_project_version(NAME)

extra = {}
if sys.version_info >= (3,):
    extra['use_2to3'] = True

classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.6",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
#     "Programming Language :: Python :: 3.2",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
]

install_requires = open("requirements.txt").read().split('\n')

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=open('README.rst', 'r').read(),
    classifiers=classifiers,
    keywords='arduino',
    author='ponty',
    # author_email='',
    url=URL,
    license='BSD',
    packages=find_packages(exclude=['bootstrap', 'pavement', ]),
    include_package_data=True,
    test_suite='nose.collector',
    zip_safe=False,
    install_requires=install_requires,
    **extra
)
