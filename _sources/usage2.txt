Usage with boards
==================

List installed boards
---------------------------

From python:

.. runblock:: pycon
    
    >>> from confduino.boardlist import boards
    >>> boards()

From console:

.. program-output:: python -m confduino.boardlist
    :prompt:

Install new board
---------------------------

Existing board will not be changed.

From python:

.. literalinclude:: ../confduino/examples/atmega88.py

console is not implemented


Remove existing board
---------------------------

From python:

    >>> from confduino.boardremove import remove_board
    >>> remove_board('diecimila')

From console::

    python -m confduino.boardremove diecimila









    