from StringIO import StringIO
from bunch import Bunch
from path import path
import ConfigParser
import logging
import tempfile
import urllib

log = logging.getLogger(__name__)

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
    config = ConfigParser.RawConfigParser()
    config.readfp(StringIO('[%s]\n' % dummy_section + s))
    bunch = AutoBunch()
    for x in config.options(dummy_section):
        cmd= 'bunch.%s = "%s"' % (x, config.get(dummy_section, x))
        exec cmd    
    return bunch

def bunch2properties(parent, data):
    lines = []
    try :
        for key, value in data.items() :
            # recursive call
            lines += bunch2properties(parent + '.' + key, value)
    except AttributeError :
        lines += [parent + '=' + data]
    return lines