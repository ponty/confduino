Usage with boards
==================

List installed boards
---------------------------

From python:

.. runblock:: pycon
    
    >>> from confduino.boardlist import boards
    >>> boards()
    >>> boards().diecimila.build.f_cpu
    >>> boards()['diecimila']['build']['f_cpu']

From console:

.. program-output:: python -m confduino.boardlist
    :prompt:

verbose (JSON compatible):

.. program-output:: python -m confduino.boardlist --verbose
    :prompt:

Help:

.. program-output:: python -m confduino.boardlist --help
    :prompt:

List installed MCUs
---------------------------

From python:

.. runblock:: pycon
    
    >>> from confduino.mculist import mcus
    >>> mcus()

From console:

.. program-output:: python -m confduino.mculist
    :prompt:

Help:

.. program-output:: python -m confduino.mculist --help
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

Help:
    
.. program-output:: python -m confduino.boardremove --help
    :prompt:






    