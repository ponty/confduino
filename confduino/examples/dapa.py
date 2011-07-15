from confduino.proginstall import install_programmer
from confduino.util import AutoBunch
from entrypoint2 import entrypoint

@entrypoint
def install(replace_existing=False):    
    'install dapa programmer'
    bunch = AutoBunch()
    bunch.name = 'DAPA'
    bunch.protocol = 'dapa'
    bunch.force = 'true'
    # bunch.delay=200
    
    install_programmer('dapa', bunch, replace_existing=replace_existing)
