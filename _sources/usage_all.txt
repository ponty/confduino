menu item "all"
====================

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
    
Help:
    
.. program-output:: python -m confduino.exampallcreate --help
    :prompt:


Result:

.. image:: menu.png


Removing  menu item 'all'
-------------------------------

From python:

    >>> from confduino.exampallremove import remove_examples_all
    >>> remove_examples_all()

From console::

    python -m confduino.exampallremove

Help:
    
.. program-output:: python -m confduino.exampallremove --help
    :prompt:



    