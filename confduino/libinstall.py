from confduino.liblist import libraries_dir
from confduino.util import tmpdir, download, clean_dir, ConfduinoError
from entrypoint2 import entrypoint
from path import path
from pyunpack import Archive
import decotrace
import logging

log = logging.getLogger(__name__)
decotrace.traced = decotrace.TraceContext(log.debug)

@decotrace.traced 
def noexample(x):
    while 1:
        f = x.next()
        if 'example' not in f.lower():
            yield f
            
@decotrace.traced 
def create_name(root):
    header_only = len(list(noexample(root.walkfiles('*.cpp')))) == 0
#    libname = None
    goodh = []
    for h in root.files('*.h'):
        cpp = h.stripext() + '.cpp'
        if  header_only or cpp.exists():
            goodh += [h]
    assert len(goodh) > 0
    log.debug('candidate headers:%s' % goodh)

    hchoosen = None
    if len(goodh) == 1:
        hchoosen = goodh[0]
    else:
        for h in goodh:
            n = h.namebase
            if n in str(root):
                hchoosen=h
        if not hchoosen:
            hchoosen = goodh[0]
            
    log.debug('choosing:%s' % hchoosen)
        
#            assert not libname
    libname = hchoosen.namebase
    return libname

@decotrace.traced 
def rename_root(root):
    name = create_name(root)
    log.debug('lib has no own dir')
    root.rename(root.parent / name)
    root = root.parent / name
    return root

@decotrace.traced 
def fix_libdir(lib_dir):
    allh = lib_dir.files('*.h')
    if len(allh) == 1:
        x = lib_dir.parent / allh[0].namebase
        lib_dir.rename(x)
        lib_dir = x
    return lib_dir

@decotrace.traced 
def find_lib_dir(root):
    '''search for lib dir under root'''
    root = path(root)
    log.debug('files in dir:' + root)
    for x in root.walkfiles():
        log.debug('  ' + x)
                
        
    # only 1 dir in root? (example: github)
    if not len(root.files()) and len(root.dirs()) == 1:
        log.debug('go inside root')
        root = root.dirs()[0]
        
    if  len(root.files('keywords.txt')):
        root = rename_root(root)
        return root, root
    
    keywords = list(root.walkfiles('keywords.txt'))
    if len(keywords):
        assert len(keywords) == 1
        lib_dir = keywords[0].parent
        lib_dir = fix_libdir(lib_dir)
        return root, lib_dir
        

    header_only = len(list(noexample(root.walkfiles('*.cpp')))) == 0
    log.debug('header_only:%s' % header_only)
    lib_dir = None
    
    headers = list(noexample(root.walkfiles('*.h')))
    
    for h in headers:
        cpp = h.stripext() + '.cpp'
        if  (header_only or cpp.exists()) and h.parent.name.lower() == h.namebase.lower():
            assert not lib_dir
            lib_dir = h.parent
            log.debug('found lib:' + lib_dir)  
    
    if not lib_dir:
        if len(headers)==1 and len(list(root.files('*.h')))==0:
            log.debug('only 1 header, not in root')
            lib_dir = headers[0].parent
            lib_dir = rename_root(lib_dir)
            
    if not lib_dir:
        # xxx.cpp and xxx.h in root? -> rename root dir
        root = rename_root(root)
        return root, root
#        for h in root.files('*.h'):
#            cpp = h.stripext() + '.cpp'
#            if  header_only or cpp.exists():
#                assert not lib_dir
#                log.debug('lib has no own dir')
#                root.rename(root.parent / h.namebase)
#                root = lib_dir = root.parent / h.namebase
    assert lib_dir
    return root, lib_dir
    
    
@decotrace.traced 
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

@decotrace.traced 
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
    if targ_dlib.exists():
        log.debug('library already exists:' + targ_dlib)
        if replace_existing:
            log.debug('remove %s' % (targ_dlib))
            targ_dlib.rmtree()
        else:
            raise ConfduinoError('library already exists:' + targ_dlib)
        
    log.debug('move %s -> %s' % (src_dlib, targ_dlib))
    src_dlib.move(targ_dlib) 
    
    libraries_dir().copymode(targ_dlib)       
    for x in targ_dlib.walk():
        libraries_dir().copymode(x)
    return targ_dlib.name       
