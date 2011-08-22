from confduino.liblist import libraries_dir
from confduino.util import tmpdir, download, clean_dir
from entrypoint2 import entrypoint
from path import path
from pyunpack import Archive
import logging

log = logging.getLogger(__name__)

 
def find_lib_dir(root):
    '''search for lib dir under root'''
    root = path(root)
    log.debug('files in dir:' + root)
    for x in root.walkfiles():
        log.debug('  ' + x)
    def noexample(x):
        while 1:
            f = x.next()
            if 'example' not in f.lower():
                yield f

    header_only = len(list(noexample(root.walkfiles('*.cpp')))) == 0
    lib_dir = None
    for h in noexample(root.walkfiles('*.h')):
        cpp = h.stripext() + '.cpp'
        if  (header_only or cpp.exists()) and h.parent.name.lower() == h.namebase.lower():
            assert not lib_dir
            lib_dir = h.parent
            log.debug('found lib:' + lib_dir)  
    
    if not lib_dir:
        # xxx.cpp and xxx.h in root? -> rename root dir
        for h in root.files('*.h'):
            cpp = h.stripext() + '.cpp'
            if  header_only or cpp.exists():
                assert not lib_dir
                log.debug('lib has no own dir')
                root.rename(root.parent / h.namebase)
                root = lib_dir = root.parent / h.namebase
    assert lib_dir
    return root, lib_dir
    
    
def move_examples(root, lib_dir):
    '''find examples not under lib dir, and move into ``examples``
    '''
    all_pde = set(root.walkfiles('*.pde'))
    lib_pde = set(lib_dir.walkfiles('*.pde'))
    stray_pde = all_pde.difference(lib_pde)
    if len(stray_pde) and not len(lib_pde):
        log.debug('examples found outside lib dir, moving them:' + str(stray_pde))
        examples = lib_dir / 'examples'
        examples.makedirs()
        for x in stray_pde:
            d = examples / x.namebase
            d.makedirs()
            x.move(d)

def fix_examples_dir(lib_dir):
    '''rename examples dir to ``examples``
    '''
    for x in lib_dir.dirs():
        if x != 'examples' and len(list(x.walkfiles('*.pde'))):
            log.debug('fixing examples dir name:' + x)
            x.rename(x.parent / 'examples')
            return

@entrypoint
def install_lib(url, replace_existing=False):
    '''install library from web or local files system
    
    :param url: web address or file path
    :param replace_existing: bool
    :rtype: None
    '''
    d = tmpdir(tmpdir())
    f = download(url)
    Archive(f).extractall(d)

    clean_dir(d)
    d, src_dlib = find_lib_dir(d)
    move_examples(d, src_dlib)
    fix_examples_dir(src_dlib)
    
    targ_dlib = libraries_dir() / src_dlib.name
    doaction = 0
    if targ_dlib.exists():
        log.debug('library already exists:' + targ_dlib)
        if replace_existing:
            log.debug('remove %s' % (targ_dlib))
            targ_dlib.rmtree()
            doaction = 1
    else:
        doaction = 1
        
    if doaction:
        log.debug('move %s -> %s' % (src_dlib, targ_dlib))
        src_dlib.move(targ_dlib) 
        
        libraries_dir().copymode(targ_dlib)       
        for x in targ_dlib.walk():
            libraries_dir().copymode(x)
            
