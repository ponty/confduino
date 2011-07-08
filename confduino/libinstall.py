from confduino.extract import extract
from confduino.liblist import libraries_dir
from confduino.util import tmpdir, download
from entrypoint2 import entrypoint
from path import path
import logging

log = logging.getLogger(__name__)

def find_lib_dir(root):
    '''search for xxx.cpp and xxx.h in xxx dir under root'''
    root = path(root)
    log.debug('files in dir:' + root)
    for x in root.walkfiles():
        log.debug('  ' + x)
    def noexample(x):
        while 1:
            f = x.next()
            if 'example' not in f.lower():
                yield f
#    print list(noexample(root.walkfiles('*.*')))
    header_only = len(list(noexample(root.walkfiles('*.cpp')))) == 0
    found = None
    for h in noexample(root.walkfiles('*.h')):
        cpp = h.stripext() + '.cpp'
        if  (header_only or cpp.exists()) and h.parent.name.lower() == h.namebase.lower():
            assert not found
            found = h.parent
            log.debug('found lib:' + found)  
    
    if not found:
        # xxx.cpp and xxx.h in root? -> rename root dir
        for h in root.files('*.h'):
            cpp = h.stripext() + '.cpp'
            if  header_only or cpp.exists():
                assert not found
                log.debug('lib has no own dir')
                root.rename(root.parent / h.namebase)
                found = root.parent / h.namebase
    assert found
    
    
    # find examples not under lib
    all_pde = set(root.walkfiles('*.pde'))
    lib_pde = set(found.walkfiles('*.pde'))
    stray_pde = all_pde.difference(lib_pde)
    if len(stray_pde):
        log.debug('examples found outside lib dir, moving them:' + str(stray_pde))
        found_examples = found / 'found_examples'
        found_examples.makedirs()
        for x in stray_pde:
            d = found_examples / x.namebase
            d.makedirs()
            x.move(d)
        
    return found

@entrypoint
def install_lib(url, replace_existing=False):
    '''install library from web or local files system
    
    :param url: web address or file path
    :param replace_existing: bool
    :rtype: None
    '''
    d = tmpdir(tmpdir())
    f = download(url)
    extract(f, d)
    src_dlib = find_lib_dir(d)
    targ_dlib = libraries_dir() / src_dlib.name
    docopy = 0
    if targ_dlib.exists():
        log.debug('library already exists:' + targ_dlib)
        if replace_existing:
            log.debug('remove %s' % (targ_dlib))
            targ_dlib.rmtree()
            docopy = 1
    else:
        docopy = 1
        
    if docopy:
        log.debug('copy %s -> %s' % (src_dlib, targ_dlib))
        src_dlib.copytree(targ_dlib)
