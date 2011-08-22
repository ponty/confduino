from confduino.hwpacklist import hwpack_dir
from entrypoint2 import entrypoint
from path import path
import logging

log = logging.getLogger(__name__)

@entrypoint
def remove_hwpack(name):
    '''remove hardware package
    
    :param name: hardware package name (e.g. 'Sanguino')
    :rtype: None
    '''
    targ_dlib = hwpack_dir() / name
    log.debug('remove %s' % (targ_dlib))
    targ_dlib.rmtree()
