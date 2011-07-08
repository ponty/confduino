Usage with programmers
==========================

List installed programmers
---------------------------

From python:

.. runblock:: pycon
    
    >>> from confduino.proglist import programmers
    >>> programmers()

From console:

.. program-output:: python -m confduino.proglist
    :prompt:

Install new programmer
---------------------------

Existing programmer will not be changed.

From python:

.. literalinclude:: ../confduino/examples/usbasp.py

console is not implemented


Remove existing programmer
---------------------------

From python:

    >>> from confduino.progremove import remove_programmer
    >>> remove_programmer('parallel')

From console::

    python -m confduino.progremove parallel









    