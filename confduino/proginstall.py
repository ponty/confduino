from confduino.proglist import programmers_txt, programmers
from confduino.progremove import remove_programmer
from confduino.util import bunch2properties
from entrypoint2 import entrypoint
import logging

log = logging.getLogger(__name__)

# TODO: how to pass options as cli argument?
       
def install_programmer(programmer_id, programmer_options, replace_existing=False):
    '''install programmer in programmers.txt
    
    :param programmer_id: string identifier
    :param programmer_options: dict like
    :param replace_existing: bool
    :rtype: None
    '''       
    doaction = 0
    if programmer_id in programmers().keys():
        log.debug('programmer already exists:' + programmer_id)
        if replace_existing:
            log.debug('remove programmer: %s' % (programmer_id))
            remove_programmer(programmer_id)
            doaction = 1
    else:
        doaction = 1
        
    if doaction:
        lines = bunch2properties(programmer_id, programmer_options)
        programmers_txt().write_lines([''] + lines, append=1)
    
    
    
    
