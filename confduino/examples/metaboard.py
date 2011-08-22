from confduino.boardinstall import install_board
from confduino.util import AutoBunch
from entrypoint2 import entrypoint

       
@entrypoint
def install_metaboard(
            replace_existing=False,
            ):    
    '''install metaboard 
    
    http://metalab.at/wiki/Metaboard
    '''
    metaboard = AutoBunch()
    metaboard.name='Metaboard'
    
    metaboard.upload.protocol='usbasp'
    metaboard.upload.maximum_size='14336'
    metaboard.upload.speed='19200'
    
    metaboard.build.mcu='atmega168'
    metaboard.build.f_cpu='16000000L'
    metaboard.build.core='arduino'
    
    metaboard.upload.disable_flushing='true'

    
    id = 'metaboard'
    
    install_board(id, metaboard, replace_existing=replace_existing)
