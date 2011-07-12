from confduino.libinstall import install_lib
from entrypoint2 import entrypoint

@entrypoint
def install(replace_existing=False):    
    'install ps2 lib'
    install_lib('http://arduino.cc/playground/uploads/Main/PS2Keyboard002.zip',
                replace_existing=replace_existing)
