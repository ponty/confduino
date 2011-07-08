from easyprocess import Proc
from path import path
import logging

log = logging.getLogger(__name__)


def extract(zip_path, target_dir):
    log.debug("extracting %s into %s" % (zip_path, target_dir))
    zip_path = path(zip_path).expand().abspath()
    target_dir = path(target_dir).expand().abspath()
    p = Proc([
                     'patool',
                     'extract',
                     zip_path,
                     '--outdir=' + target_dir
                     ]).call()
    assert p.return_code == 0, p
