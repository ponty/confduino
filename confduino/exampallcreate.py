from confduino.exampallremove import remove_examples_all
from confduino.examplist import examples_all_dir
from confduino.liblist import libraries, lib_examples, lib_example_dir
from entrypoint2 import entrypoint
import logging
import os

log = logging.getLogger(__name__)

@entrypoint
def create_examples_all():
    '''create arduino/examples/all directory 

    :rtype: None
    '''
    remove_examples_all()
    examples_all_dir().mkdir()
           
    for lib in libraries():
        maindir = examples_all_dir() / lib.upper()[0:1] / lib
#        libraries_dir() / 
        maindir.makedirs_p()
        
        for ex in  lib_examples(lib):
            d=lib_example_dir(lib, ex)
            if hasattr(os, 'symlink'):
                d.symlink(maindir / ex)
            else:
                d.copytree(maindir / ex)
