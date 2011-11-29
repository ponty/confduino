from confduino import exampallcreate
from confduino.libinstall import install_lib
from confduino.util import ConfduinoError
from entrypoint2 import entrypoint
    
   
@entrypoint
def upgrade_many(upgrade=True, create_examples_all=True):    
    '''upgrade many libs
    
    source: http://arduino.cc/playground/Main/LibraryList

    you can set your arduino path if it is not default
    os.environ['ARDUINO_HOME'] = '/home/...'
    '''
    urls=set()
    def inst(url):
        print 'upgrading ' + url
        assert url not in urls
        urls.add(url)
        try:
            lib = install_lib(url, upgrade)
            print ' -> ', lib
        except ConfduinoError as e:
            print e
            

    ############################
    # github.com
    ############################
    inst('https://github.com/madsci1016/Arduino-EasyTransfer/zipball/master')
    inst('https://github.com/madsci1016/Arduino-SoftEasyTransfer/zipball/master')
    inst('https://github.com/madsci1016/Arduino-PS2X/zipball/master')
#    inst('http://github.com/wimleers/flexitimer2/zipball/v1.0')# can't install
    inst('https://github.com/kerinin/arduino-splines/zipball/master')
    inst('https://github.com/asynclabs/WiShield/zipball/master')   
    inst('https://github.com/asynclabs/dataflash/zipball/master') 
    inst('https://github.com/slugmobile/AtTouch/zipball/master')
    inst('https://github.com/carlynorama/Arduino-Library-Button/zipball/master')
    inst('https://github.com/carlynorama/Arduino-Library-FancyLED/zipball/master')
    inst('https://github.com/markfickett/arduinomorse/zipball/master')
    
      
    ############################
    # arduiniana.org
    ############################
    # TODO: how to get latest version?? 
    inst('http://arduiniana.org/PString/PString2.zip')
    inst('http://arduiniana.org/Flash/Flash3.zip')
    inst('http://arduiniana.org/NewSoftSerial/NewSoftSerial10c.zip')
    inst('http://arduiniana.org/Streaming/Streaming4.zip')
    inst('http://arduiniana.org/PWMServo/PWMServo.zip')
    inst('http://arduiniana.org/TinyGPS/TinyGPS10.zip')


    ############################
    # google
    ############################
    # TODO: how to get latest version?? 
    # parse http://code.google.com/p/arduino-pinchangeint/downloads/list

#    inst('http://rogue-code.googlecode.com/files/Arduino-Library-Tone.zip') # already in core!
    inst('http://arduino-playground.googlecode.com/files/LedDisplay03.zip')
    inst('http://sserial2mobile.googlecode.com/files/SSerial2Mobile-1.1.0.zip')
    inst('http://webduino.googlecode.com/files/webduino-1.4.1.zip')# can't install
    inst('http://arduino-pid-library.googlecode.com/files/PID_v1.0.1.zip')
    inst('http://ideoarduinolibraries.googlecode.com/files/Qtouch1Wire.zip')
    inst('http://arduino-timerone.googlecode.com/files/TimerOne-v8.zip')
    inst('http://arduinounit.googlecode.com/files/arduinounit-1.4.2.zip')
    inst('http://arduinode.googlecode.com/files/arduinode_0.1.zip')
    inst('http://arduino-edb.googlecode.com/files/EDB_r7.zip')
    inst('http://arduino-dblib.googlecode.com/files/DB.zip')
    inst('http://morse-endecoder.googlecode.com/files/Morse_EnDecoder_2010.12.06.tar.gz')
    inst('http://arduino-pinchangeint.googlecode.com/files/PinChangeInt.zip')
    
    ############################
    # others
    ############################
    inst('http://download.milesburton.com/Arduino/MaximTemperature/DallasTemperature_370Beta.zip')
    inst('http://www.pjrc.com/teensy/arduino_libraries/OneWire.zip')
    inst('http://interface.khm.de/wp-content/uploads/2009/01/FreqCounter1.zip')
#    inst('http://www.state-machine.com/arduino/qp_arduino.zip') # too big
    inst('ftp://momjian.us/pub/arduino/TButton.zip') # AdvButton is better
    inst('http://johnmchilton.com/media/UComms.zip')
    inst('http://www.shikadi.net/files/arduino/SerialIP-1.0.zip')
    inst('http://siggiorn.com/wp-content/uploads/libraries/ArduinoByteBuffer.zip')
    inst('http://siggiorn.com/wp-content/uploads/libraries/ArduinoSerialManager.zip')
    inst('http://arduino-tweet.appspot.com/Library-Twitter-1.2.2.zip')    
#    inst('http://gkaindl.com/php/download.php?key=ArduinoEthernet')# can't install
    inst('http://geekcowboy.net/downloads/x10.zip')
    inst('http://sebastian.setz.name/wp-content/uploads/2011/01/multiCameraIrControl_1-5.zip')
    inst('http://www.familjenlinder.se/Morse.7z')
    inst('http://www.pjrc.com/teensy/arduino_libraries/FrequencyTimer2.zip')
    inst('http://alexandre.quessy.net/static/avr/Tween_01.zip')
    inst('http://www.lpelettronica.it/images/stories/LPM11162_images/Arduino/LPM11162_ArduinoLib_v1.zip')
    
    ############################
    # arduino.cc
    ############################
    inst('http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip')
    inst('http://arduino.cc/playground/uploads/Code/Metro.zip')
    inst('http://www.arduino.cc/playground/uploads/Main/MsTimer2.zip')
#    inst('http://www.arduino.cc/playground/uploads/Code/Time.zip')# can't install
    inst('http://arduino.cc/playground/uploads/Main/LedControl.zip')
#    inst('http://www.arduino.cc/playground/uploads/Code/ks0108GLCD.zip')# can't install
    inst('http://arduino.cc/playground/uploads/Code/Bounce.zip')
    inst('http://arduino.cc/playground/uploads/Main/CapacitiveSense003.zip')
    inst('http://arduino.cc/playground/uploads/Main/PinChangeInt.zip')
#    inst('http://arduino.cc/playground/uploads/Code/TimerThree.zip')# can't install
    inst('http://arduino.cc/playground/uploads/Code/TimedAction-1_6.zip')
#    inst('http://www.arduino.cc/playground/uploads/Code/Time.zip')# can't install
    inst('http://arduino.cc/playground/uploads/Code/EventFuse.zip')
    inst('http://arduino.cc/playground/uploads/Code/Charlieplex.zip')
    inst('http://arduino.cc/playground/uploads/Code/DigitalToggle.zip')
    inst('http://arduino.cc/playground/uploads/Code/Enerlib.zip')
    
    inst('http://arduino.cc/playground/uploads/Code/AdvButton_11.zip')
    #inst('http://arduino.cc/playground/uploads/Code/AdvButton.zip') # old version
    
#    inst('http://arduino.cc/playground/uploads/Code/SerialDebugger.zip') # can't install
    inst('http://arduino.cc/playground/uploads/Code/MatrixMath.zip')
      
    inst('http://arduino.cc/playground/uploads/Code/StackArray.zip')
    inst('http://arduino.cc/playground/uploads/Code/StackList.zip')
    inst('http://arduino.cc/playground/uploads/Code/QueueArray.zip')
    inst('http://arduino.cc/playground/uploads/Code/QueueList.zip')
    inst('http://arduino.cc/playground/uploads/Code/Ping-1_3.zip')
    inst('http://www.arduino.cc/playground/uploads/Code/LED.zip')
    
#    inst('')
    if create_examples_all:
        print 'create "all" menu item'
        exampallcreate.create_examples_all()
    print 'install finished'

