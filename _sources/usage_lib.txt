Usage with libraries
====================

List installed libraries
---------------------------

From python:

.. runblock:: pycon
    
    >>> from confduino.liblist import libraries
    >>> libraries()

From console:

.. program-output:: python -m confduino.liblist
    :prompt:

Help:

.. program-output:: python -m confduino.liblist --help
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

Help:

.. program-output:: python -m confduino.libinstall --help
    :prompt:

Remove existing library
---------------------------

From python:

    >>> from confduino.libremove import remove_lib
    >>> remove_lib('PS2Keyboard')

From console::

    python -m confduino.libremove PS2Keyboard

Help:

.. program-output:: python -m confduino.libremove --help
    :prompt:



    