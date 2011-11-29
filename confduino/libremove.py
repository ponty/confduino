from confduino.liblist import libraries_dir
from entrypoint2 import entrypoint
import logging

log = logging.getLogger(__name__)

@entrypoint
def remove_lib(lib_name):
    '''remove library
    
    :param lib_name: library name (e.g. 'PS2Keyboard')
    :rtype: None
    '''
    targ_dlib = libraries_dir() / lib_name
    log.debug('remove %s' % (targ_dlib))
    targ_dlib.rmtree()
