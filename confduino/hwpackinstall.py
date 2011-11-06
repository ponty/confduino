from confduino.hwpacklist import hwpack_dir
from confduino.util import tmpdir, download, clean_dir
from entrypoint2 import entrypoint
from path import path
from pyunpack import Archive
import logging

log = logging.getLogger(__name__)

    
    
def find_hwpack_dir(root):
    '''search for hwpack dir under root'''
    root = path(root)
    log.debug('files in dir:' + root)
    for x in root.walkfiles():
        log.debug('  ' + x)
        
    hwpack_dir = None
    for h in (root.walkfiles('boards.txt')):
        assert not hwpack_dir
        hwpack_dir = h.parent
        log.debug('found hwpack:' + hwpack_dir)  
    
    assert hwpack_dir
    return hwpack_dir
    
    

@entrypoint
def install_hwpack(url, replace_existing=False):
    '''install hwpackrary from web or local files system
    
    :param url: web address or file path
    :param replace_existing: bool
    :rtype: None
    '''
    d = tmpdir(tmpdir())
    f = download(url)
    Archive(f).extractall(d)

    clean_dir(d)
    src_dhwpack = find_hwpack_dir(d)
    
    targ_dhwpack = hwpack_dir() / src_dhwpack.name
    doaction = 0
    if targ_dhwpack.exists():
        log.debug('hwpack already exists:' + targ_dhwpack)
        if replace_existing:
            log.debug('remove %s' % (targ_dhwpack))
            targ_dhwpack.rmtree()
            doaction = 1
    else:
        doaction = 1
        
    if doaction:
        log.debug('move %s -> %s' % (src_dhwpack, targ_dhwpack))
        src_dhwpack.move(targ_dhwpack) 
        
        hwpack_dir().copymode(targ_dhwpack)       
        for x in targ_dhwpack.walk():
            hwpack_dir().copymode(x)
            
