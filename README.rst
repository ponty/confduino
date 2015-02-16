confduino is an Arduino_ library, programmer, board configurator

Links:
 * home: https://github.com/ponty/confduino
 * documentation: http://ponty.github.com/confduino
 
.. image:: https://pypip.in/version/confduino/badge.svg
    :target: https://pypi.python.org/pypi/confduino/
    :alt: Latest Version

.. image:: https://pypip.in/py_versions/confduino/badge.svg
    :target: https://pypi.python.org/pypi/confduino/
    :alt: Supported Python versions

.. image:: https://pypip.in/license/confduino/badge.svg
    :target: https://pypi.python.org/pypi/confduino/
    :alt: License
            
.. image:: https://pypip.in/download/confduino/badge.svg
    :target: https://pypi.python.org/pypi/confduino/
    :alt: Downloads
    
.. image:: https://travis-ci.org/ponty/confduino.svg?branch=master
    :target: https://travis-ci.org/ponty/confduino
    :alt: Build
        
.. image:: https://coveralls.io/repos/ponty/confduino/badge.svg?branch=master
    :target: https://coveralls.io/r/ponty/confduino?branch=master
    :alt: Coverage

.. image:: https://landscape.io/github/ponty/confduino/master/landscape.svg?style=flat
    :target: https://landscape.io/github/ponty/confduino/master
    :alt: Code Health
   
Features:
 - get Arduino_ version
 - list, install, remove Arduino_ libraries
    - install libraries from internet or local drive
    - fix ``examples`` directory name before installing
    - clean library (.*,_*,..) before installing
    - move examples under ``examples`` directory
    - upgrade library to 1.0: replace ``#include "wprogram.h"`` with ``#include "Arduino.h"``
 - list, install, remove Arduino_ programmers
 - list, install, remove Arduino_ boards
 - can be used as a python library or as a console program
 - unpacker back-end: pyunpack_
 - downloader back-end: urllib_
 - some functionality is based on arscons_
 - supported python versions: 2.6, 2.7, 3.3, 3.4
 - supported Arduino versions: 1.0.5
 
Known problems:
 - tested only on linux
 - some libraries with unusual structure can not be installed

arduino libraries: http://www.arduino.cc/en/Reference/Libraries
 
Basic usage
===========

install library:

    >>> from confduino.libinstall import install_lib
    >>> install_lib('http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip')

or on console::

    python -m confduino.libinstall http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip

install a lot of libraries::

    python -m confduino.libinstall.examples.upgrademany

Installation
============

General
-------

 * install arduino_
 * install python_
 * install pip_
 * install back-ends for pyunpack_ (optional)
 * install the program::

    # as root
    pip install confduino
    


Ubuntu
------
::

    sudo apt-get install arduino
    sudo apt-get install python-pip
    sudo pip install confduino
    sudo apt-get install unzip unrar p7zip-full

Uninstall
---------

::

    # as root
    pip uninstall confduino


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _arduino: http://arduino.cc/
.. _python: http://www.python.org/
.. _urllib: http://docs.python.org/library/urllib.html
.. _arscons: http://code.google.com/p/arscons/
.. _pyunpack: https://github.com/ponty/pyunpack
