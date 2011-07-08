from confduino.boardinstall import install_board
from confduino.util import AutoBunch
from entrypoint2 import entrypoint

@entrypoint
def install():    
    'install atmega88 board'
    atmega88 = AutoBunch()
    atmega88.name='Atmega88 usbasp 16MHz'
    
    atmega88.upload.using='usbasp'
    
    atmega88.build.mcu='atmega88'
    atmega88.build.f_cpu='16000000L'
    atmega88.build.core='arduino'
    
    install_board('atmega88', atmega88, replace_existing=0)
