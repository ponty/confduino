from six import StringIO
from munch import Munch
from path import Path as path
from six.moves import configparser
import logging
import tempfile
import urllib

log = logging.getLogger(__name__)


class ConfduinoError(Exception):
    pass


def tmpdir(directory=None, suffix=''):
    x = tempfile.mkdtemp(suffix=suffix, prefix='confduino_', dir=directory)
    return path(x)


def download(url):
    log.debug('downloading %s', url)
    f, _ = urllib.urlretrieve(url)
    log.debug('downloaded file: %s', f)
    return f


class AutoBunch (Munch):

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

    def __setattr__(self, k, v):
        """Recursive.

        >>> x=AutoBunch()
        >>> setattr(x, 'mega.name', 'xy')

        """
        k2, _, k3 = k.partition('.')
        if k3:
            self.__getattr__(k2).__setattr__(k3, v)
        else:
            Munch.__setattr__(self, k, v)


def read_properties(filename):
    """read properties file into bunch.

    :param filename: string
    :rtype: bunch (dict like and object like)

    """
    s = path(filename).text()
    dummy_section = 'xxx'
    cfgparser = configparser.RawConfigParser()

    # avoid converting options to lower case
    cfgparser.optionxform = str

    cfgparser.readfp(StringIO('[%s]\n' % dummy_section + s))
    bunch = AutoBunch()
    for x in cfgparser.options(dummy_section):
        setattr(bunch, x, cfgparser.get(dummy_section, str(x)))
    return bunch


def bunch2properties(parent, data):
    lines = []
    try:
        for key, value in data.items():
            # recursive call
            lines += bunch2properties(parent + '.' + key, value)
    except AttributeError:
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
