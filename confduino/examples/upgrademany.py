from confduino.libinstall import install_lib
from entrypoint2 import entrypoint
    
UPGRADE = True

def upgrade(url):
    print 'upgrading ' + url
    install_lib(url, UPGRADE)
    
@entrypoint
def upgrade_many():    
    'upgrade many libs'

    # you can set your arduino path if it is not default
    #os.environ['ARDUINO_HOME'] = '/home/...'
    
    ############################
    # arduino.cc
    ############################
    upgrade('http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip')
    upgrade('http://arduino.cc/playground/uploads/Code/Metro.zip')
    upgrade('http://www.arduino.cc/playground/uploads/Main/MsTimer2.zip')
#    upgrade('http://www.arduino.cc/playground/uploads/Code/Time.zip')
#    upgrade('http://arduino.cc/playground/uploads/Main/LedControl.zip')
#    upgrade('http://www.arduino.cc/playground/uploads/Code/ks0108GLCD.zip')
    upgrade('http://arduino.cc/playground/uploads/Code/Bounce.zip')
    upgrade('http://arduino.cc/playground/uploads/Main/CapacitiveSense003.zip')
    upgrade('http://arduino.cc/playground/uploads/Main/PinChangeInt.zip')
#    upgrade('http://arduino.cc/playground/uploads/Code/TimerThree.zip')
    upgrade('http://arduino.cc/playground/uploads/Code/TimedAction-1_6.zip')
#    upgrade('http://www.arduino.cc/playground/uploads/Code/Time.zip')
    upgrade('http://arduino.cc/playground/uploads/Code/EventFuse.zip')
    upgrade('http://arduino.cc/playground/uploads/Code/Charlieplex.zip')
    upgrade('http://arduino.cc/playground/uploads/Code/DigitalToggle.zip')
    upgrade('http://arduino.cc/playground/uploads/Code/Enerlib.zip')
    
    upgrade('http://arduino.cc/playground/uploads/Code/AdvButton_11.zip')
    #upgrade('http://arduino.cc/playground/uploads/Code/AdvButton.zip') # old version
    
#    upgrade('http://arduino.cc/playground/uploads/Code/SerialDebugger.zip') # can't install
      
    ############################
    # arduiniana.org
    ############################
    # TODO: how to get latest version?? 
    upgrade('http://arduiniana.org/PString/PString2.zip')
    upgrade('http://arduiniana.org/Flash/Flash3.zip')
    upgrade('http://arduiniana.org/NewSoftSerial/NewSoftSerial10c.zip')
    upgrade('http://arduiniana.org/Streaming/Streaming4.zip')
#    upgrade('http://arduiniana.org/PWMServo/PWMServo.zip')
#    upgrade('http://arduiniana.org/TinyGPS/TinyGPS10.zip')


    ############################
    # google
    ############################

#    upgrade('http://rogue-code.googlecode.com/files/Arduino-Library-Tone.zip') # already in core!

#    upgrade('http://arduino-playground.googlecode.com/files/LedDisplay03.zip')
    upgrade('http://sserial2mobile.googlecode.com/files/SSerial2Mobile-1.1.0.zip')
#    upgrade('http://webduino.googlecode.com/files/webduino-1.4.1.zip')
    upgrade('http://arduino-pid-library.googlecode.com/files/PID_v1.0.1.zip')
    upgrade('http://ideoarduinolibraries.googlecode.com/files/Qtouch1Wire.zip')
    upgrade('http://arduino-timerone.googlecode.com/files/TimerOne-v2.zip')


    ############################
    # others
    ############################
    upgrade('http://download.milesburton.com/Arduino/MaximTemperature/DallasTemperature_370Beta.zip')
    upgrade('http://www.pjrc.com/teensy/arduino_libraries/OneWire.zip')
    upgrade('http://interface.khm.de/wp-content/uploads/2009/01/FreqCounter1.zip')
#    upgrade('http://github.com/wimleers/flexitimer2/zipball/v1.0')
#    upgrade('http://www.state-machine.com/arduino/qp_arduino.zip')
#    upgrade('ftp://momjian.us/pub/arduino/TButton.zip') # AdvButton is better
    upgrade('http://johnmchilton.com/media/UComms.zip')
    upgrade('http://www.shikadi.net/files/arduino/SerialIP-1.0.zip')
