Examples
========

Install libraries
-----------------

Many libraries are upgraded in examples/upgrademany.py, this can be started::

    python -m confduino.examples.upgrademany

Code:

.. literalinclude:: ../confduino/examples/upgrademany.py


Install STK200 programmer
-------------------------

::

    python -m confduino.examples.stk200

Code:

.. literalinclude:: ../confduino/examples/stk200.py

Install atmega88 board
----------------------

::

    python -m confduino.examples.atmega88

Code:

.. literalinclude:: ../confduino/examples/atmega88.py

options:

.. program-output:: python -m confduino.examples.atmega88 --help
    :prompt:

    
remove boards
-------------
    
.. program-screenshot:: python -m confduino.examples.remove_boards
    :prompt:
    
.. program-screenshot:: python -m confduino.examples.remove_boards --hwpack arduino
    :prompt:

Code:

.. literalinclude:: ../confduino/examples/remove_boards.py

remove libraries
----------------
    
.. program-screenshot:: python -m confduino.examples.remove_libraries
    :prompt:
    

Code:

.. literalinclude:: ../confduino/examples/remove_libraries.py
    