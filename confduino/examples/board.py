from confduino.boardinstall import install_board
from confduino.util import AutoBunch
from entrypoint2 import entrypoint

def strfreq(f):
    if f >= 1000000:
        s = str(f / 1000000.0) + 'MHz'
    elif f >= 1000:
        s = str(f / 1000.0) + 'kHz'
    else:
        s = str(f) + 'Hz'
    return s    
        
@entrypoint
def install_board_with_programmer(mcu, 
            programmer, 
            f_cpu=16000000, 
            core='arduino',
            replace_existing=False,
            ):    
    'install board with programmer'
    bunch = AutoBunch()
    id = '{mcu}_{f_cpu}_{programmer}'.format(f_cpu=f_cpu,
                                                 mcu=mcu,
                                                 programmer=programmer,
                                                 )
    bunch.name = '{mcu}@{f} Prog:{programmer}'.format(f=strfreq(f_cpu),
                                                 mcu=mcu,
                                                 programmer=programmer,
                                                 )
    
    bunch.upload.using = programmer
    
    bunch.build.mcu = mcu
    bunch.build.f_cpu = str(f_cpu) + 'L'
    bunch.build.core = core
    
    install_board(id, bunch, replace_existing=replace_existing)
