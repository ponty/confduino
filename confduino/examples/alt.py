from confduino.hwpackinstall import install_hwpack
from entrypoint2 import entrypoint

@entrypoint
def install(replace_existing=False):    
    'install alternate CORE files'
    install_hwpack('http://www.avr-developers.com/corefiles/arduino-extras.zip',
                replace_existing=replace_existing)
