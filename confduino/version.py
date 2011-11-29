from confduino import arduino_path
from entrypoint2 import entrypoint

def version_txt():
    '''return version.txt path
    
    $ARDUINO/lib/version.txt
    '''
    x = arduino_path() / 'lib' / 'version.txt'
    return x

def version():
    '''return version
    
    example: 0022
    '''
    return version_txt().text()

@entrypoint
def print_version():
    '''print arduino version
    
    example: 0022
    '''
    print version()
