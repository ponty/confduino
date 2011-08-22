from confduino.hwpackinstall import install_hwpack
from entrypoint2 import entrypoint

@entrypoint
def install(replace_existing=False):    
    'install sanguino hardware package'
    install_hwpack('http://sanguino.googlecode.com/files/Sanguino-0018r2_1_4.zip',
                replace_existing=replace_existing)
