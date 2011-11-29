Usage with libraries
====================

Arduino path
-------------

If Arduino can not be found at default path,
then ``ARDUINO_HOME`` environment variable 
should be set.

on Ubuntu:
in ``~/.profile``::

    ARDUINO_HOME=~/opt/arduino
    export ARDUINO_HOME

Default path:
 * Mac: /Applications/Arduino.app/Contents/Resources/Java 
 * Linux: /usr/share/arduino/


List installed libraries
---------------------------

From python:

.. runblock:: pycon
    
    >>> from confduino.liblist import libraries
    >>> libraries()

From console:

.. program-output:: python -m confduino.liblist
    :prompt:

Install new library
---------------------------

Existing library will not be changed.

From python:

    >>> from confduino.libinstall import install_lib
    >>> install_lib('http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip')

From console::

    python -m confduino.libinstall http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip
    
Upgrade existing library
---------------------------

Same as install with *replace_existing* option.

From python:

    >>> from confduino.libinstall import install_lib
    >>> install_lib('http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip', replace_existing=1)

From console::

    python -m confduino.libinstall http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip --replace-existing


Remove existing library
---------------------------

From python:

    >>> from confduino.libremove import remove_lib
    >>> remove_lib('PS2Keyboard')

From console::

    python -m confduino.libremove PS2Keyboard


Create menu item "all" for examples
--------------------------------------------

If you have a lot of libraries and low screen resolution 
then all menu items under "examples" can not be accessed.

Bug report: "Long menus don't scroll" (http://code.google.com/p/arduino/issues/detail?id=426)

My workaround creates a 2 level deep menu structure 
without changing other menu items. Symbolic links are used if possible.

From python:

    >>> from confduino.exampallcreate import create_examples_all
    >>> create_examples_all()

From console::

    python -m confduino.exampallcreate


Result:

.. image:: menu.png


Removing  menu item 'all'
-------------------------------

From python:

    >>> from confduino.exampallremove import remove_examples_all
    >>> remove_examples_all()

From console::

    python -m confduino.exampallremove




    