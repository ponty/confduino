from confduino.hwpackinstall import install_hwpack
from entrypoint2 import entrypoint


@entrypoint
def install(replace_existing=False):
    """install sanguino hardware package."""
    install_hwpack(
        'https://sanguino.googlecode.com/files/Sanguino-0101r1.zip',
        replace_existing=replace_existing)
