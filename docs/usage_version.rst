Check Arduino version
======================


From python
---------------------------

.. runblock:: pycon
    
    >>> from confduino.version import version, intversion, sketch_extension
    >>> from confduino import set_arduino_path
    >>>
    >>> version()
    >>> intversion()
    >>> sketch_extension()
    >>>
    >>> set_arduino_path('~/opt/arduino-0022')
    >>> version()
    >>> intversion()
    >>> sketch_extension()
    >>>
    >>> set_arduino_path('~/opt/arduino-1.0')
    >>> version()
    >>> intversion()
    >>> sketch_extension()

From console
---------------------------

.. program-output:: python -m confduino.version
    :prompt:

Help:

.. program-output:: python -m confduino.version --help
    :prompt:

Examples
---------------------------

.. program-output:: env ARDUINO_HOME=~/opt/arduino-0022 python -m confduino.version
    :prompt:
    :shell:

.. program-output:: env ARDUINO_HOME=~/opt/arduino-0022 python -m confduino.version --integer
    :prompt:
    :shell:

.. program-output:: env ARDUINO_HOME=~/opt/arduino-1.0 python -m confduino.version
    :prompt:
    :shell:

.. program-output:: env ARDUINO_HOME=~/opt/arduino-1.0 python -m confduino.version --integer
    :prompt:
    :shell:



    