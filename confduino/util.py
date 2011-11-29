from StringIO import StringIO
from bunch import Bunch
from path import path
import ConfigParser
import logging
import tempfile
import urllib

log = logging.getLogger(__name__)

class ConfduinoError(Exception):
    pass

def tmpdir (dir=None, suffix=''):
    x= tempfile.mkdtemp(suffix=suffix, prefix='confduino_', dir=dir)
    return path(x)

def download(url):
    log.debug("downloading " + url)
    f, _ = urllib.urlretrieve(url)
    log.debug("downloaded file:" + f)
    return f

class AutoBunch (Bunch):
    def __getattr__(self, k):
        '''
        Bunch is created for missing keys:
        
        >>> x=AutoBunch()
        >>> x.mega.name = 'xy'
        '''
        try:
            return self[k]
        except KeyError:
#            raise AttributeError(k)
            self[k] = AutoBunch()
            return self[k]

def read_properties(filename):
    ''' read properties file into bunch
    
    :param filename: string
    :rtype: bunch (dict like and object like)
    '''
    s = path(filename).text()
    dummy_section = 'xxx'
    cfgparser = ConfigParser.RawConfigParser()
    
    # avoid converting options to lower case
    cfgparser.optionxform = str
    
    cfgparser.readfp(StringIO('[%s]\n' % dummy_section + s))
    bunch = AutoBunch()
    for x in cfgparser.options(dummy_section):
        cmd= 'bunch.%s = "%s"' % (x, cfgparser.get(dummy_section, x))
        exec cmd    
    return bunch

def bunch2properties(parent, data):
    lines = []
    try :
        for key, value in data.items() :
            # recursive call
            lines += bunch2properties(parent + '.' + key, value)
    except AttributeError :
        lines += [parent + '=' + str(data)]
    return lines

def clean_dir(root):
    '''remove .* and _* files and directories under root'''
    for x in root.walkdirs('.*', errors='ignore'):
        x.rmtree()
    for x in root.walkdirs('_*', errors='ignore'):
        x.rmtree()

    for x in root.walkfiles('.*', errors='ignore'):
        x.remove()
    for x in root.walkfiles('_*', errors='ignore'):
        x.remove()
