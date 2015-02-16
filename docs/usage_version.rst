Check Arduino version
=====================


From python
-----------

.. runblock:: pycon
    
    >>> from confduino.version import version, intversion, sketch_extension
    >>> from confduino import set_arduino_path
    >>>
    >>> version()
    >>> intversion()
    >>> sketch_extension()
    >>>

From console
------------

.. program-output:: python -m confduino.version
    :prompt:

Help:

.. program-output:: python -m confduino.version --help
    :prompt:


    