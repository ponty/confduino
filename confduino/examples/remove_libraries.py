from confduino.liblist import libraries, libraries_dir
from confduino.libremove import remove_lib
from entrypoint2 import entrypoint
import psidialogs

        
@entrypoint
def gui():    
    'remove libraries by GUI'

    sel = psidialogs.multi_choice(libraries(),
                            'select libraries to remove from %s!' % libraries_dir(),
                            title='remove boards')
    print sel, 'selected'

    if sel:
        if psidialogs.ask_yes_no('Do you really want to remove selected libraries?\n'+'\n'.join(sel)):
            for x in sel:
                remove_lib(x)
                print x + ' was removed'
