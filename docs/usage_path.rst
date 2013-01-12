Arduino path
====================

If Arduino can not be found at default path,
then ``ARDUINO_HOME`` environment variable 
should be set.

on Ubuntu (https://help.ubuntu.com/community/EnvironmentVariables):
in ``~/.profile``::

    ARDUINO_HOME=~/opt/arduino
    export ARDUINO_HOME

temporary changes:

.. program-output:: env ARDUINO_HOME=~/opt/arduino-0022 python -m confduino.version
    :prompt:
    :shell:

.. program-output:: env ARDUINO_HOME=~/opt/arduino-1.0 python -m confduino.version
    :prompt:
    :shell:


Default path:
 * Mac: /Applications/Arduino.app/Contents/Resources/Java 
 * Linux: /usr/share/arduino/

