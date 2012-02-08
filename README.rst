confduino is an arduino_ library configurator

Links:
 * home: https://github.com/ponty/confduino
 * documentation: http://ponty.github.com/confduino
 
Features:
 - list, install, remove arduino_ libraries
 - install libraries from internet or local drive
 - fix ``examples`` directory name before installing
 - clean library (.*,_*,..) before installing
 - move examples under ``examples`` directory
 - list, install, remove arduino_ programmers
 - list, install, remove arduino_ boards
 - written in python
 - crossplatform
 - can be used as a python library or as a console program
 - unpacker backend: pyunpack_
 - downloader backend: urllib_
 - some functionality is based on arscons_
 
Known problems:
 - Python 3 is not supported
 - tested only on linux
 - tested only with arduino version 0022
 - some libraries with unusual structure can not be installed
 - not all commands have console interface

arduino libraries: http://www.arduino.cc/en/Reference/Libraries
 
Basic usage
============

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
--------

 * install arduino_
 * install python_
 * install pip_
 * install backends for pyunpack_ (optional)
 * install the program::

    # as root
    pip install confduino
    


Ubuntu
----------
::

    sudo apt-get install arduino
    sudo apt-get install python-pip
    sudo pip install confduino
    sudo apt-get install unzip unrar p7zip-full

Uninstall
----------

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
