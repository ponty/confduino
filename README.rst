confduino is an arduino_ library configurator

Links:
 * home: https://github.com/ponty/confduino
 * documentation: http://ponty.github.com/confduino
 * arduino libraries: http://www.arduino.cc/en/Reference/Libraries
 
Features:
 - list, install, remove arduino_ libraries
 - install libraries from internet or local drive
 - fix ``examples`` directory name
 - clean library (.*,_*,..)
 - move examples to right location
 - list, install, remove arduino_ programmers
 - list, install, remove arduino_ boards
 - written in python
 - crossplatform
 - can be used as a python library or as a console program
 - unpacker backend: patool_
 - downloader backend: urllib_
 
Known problems:
 - Python 3 is not supported
 - tested only on linux
 - some libraries with unusual structure can not be installed
 - not all commands have console interface
 
Basic usage
============

install library:

    >>> from confduino.libinstall import install_lib
    >>> install_lib('http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip')

or on console::

    python -m confduino.libinstall http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip


Installation
============

General
--------

 * install arduino_
 * install python_
 * install setuptools_
 * install unpackers for patool_
 * install patool_ (easy_install does not work)
 * install the program::

    # as root
    easy_install confduino
    


Ubuntu
----------
::

    sudo apt-get install arduino
    sudo apt-get install python-setuptools
    sudo apt-get install unzip
    sudo easy_install http://sourceforge.net/projects/patool/files/0.13/patool-0.13.tar.gz/download
    sudo easy_install confduino

Uninstall
----------

first install pip_::

    # as root
    pip uninstall confduino


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _arduino: http://arduino.cc/
.. _python: http://www.python.org/
.. _urllib: http://docs.python.org/library/urllib.html
.. _patool: http://pypi.python.org/pypi/patool