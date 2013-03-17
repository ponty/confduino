from bunch import Bunch

TEST_ARDUINO_INSTALLATIONS = [
    Bunch(path='~/opt/arduino-0022', ver='0022', iver=22),
    Bunch(path='~/opt/arduino-1.0', ver='1.0', iver=100),
    Bunch(path='~/opt/arduino-1.0.3', ver='1.0.3', iver=103),
    Bunch(path='/usr/share/arduino', ver='1.0.1', iver=101),
]

TEST_ARDUINO_PATHS = [x.path for x in TEST_ARDUINO_INSTALLATIONS]
