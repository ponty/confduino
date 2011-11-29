from confduino.examplist import examples_all_dir
from entrypoint2 import entrypoint
import logging

log = logging.getLogger(__name__)

@entrypoint
def remove_examples_all():
    '''remove arduino/examples/all directory 

    :rtype: None
    '''
    d = examples_all_dir()
    if d.exists():
        log.debug('remove %s' % (d))
        d.rmtree()
    else:
        log.debug('nothing to remove:%s' % (d))
