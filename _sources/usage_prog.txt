Usage with programmers
==========================

List installed programmers
---------------------------

From python:

.. runblock:: pycon
    
    >>> from confduino.proglist import programmers
    >>> programmers()
    >>> programmers().arduinoisp.speed
    >>> programmers()['arduinoisp']['speed']

From console:

.. program-output:: python -m confduino.proglist
    :prompt:

verbose (JSON compatible):

.. program-output:: python -m confduino.proglist --verbose
    :prompt:

Help:

.. program-output:: python -m confduino.proglist --help
    :prompt:

Install new programmer
---------------------------

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

Help:

.. program-output:: python -m confduino.progremove --help
    :prompt:






    