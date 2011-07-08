from confduino.proginstall import install_programmer
from confduino.util import AutoBunch
from entrypoint2 import entrypoint

@entrypoint
def install():    
    'install usbasp programmer'
    usbasp = AutoBunch()
    usbasp.name = 'usbasp'
    usbasp.communication = 'usb'
    usbasp.protocol = 'usbasp'
    
    install_programmer('usbasp', usbasp, replace_existing=0)
