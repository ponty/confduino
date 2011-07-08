from confduino.proglist import programmers_txt
from entrypoint2 import entrypoint
from path import path
import logging

log = logging.getLogger(__name__)

@entrypoint
def remove_programmer(programmer_id):
    '''remove programmer
    
    :param programmer_id: programmer id (e.g. 'avrisp')
    :rtype: None
    '''

    log.debug('remove %s' % (programmer_id))
    lines = programmers_txt().lines()
    lines = filter(lambda x: not x.strip().startswith(programmer_id + '.'), lines)
    programmers_txt().write_lines(lines)