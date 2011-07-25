from confduino.boardlist import boards, boards_txt
from confduino.boardremove import remove_board
from entrypoint2 import entrypoint
import psidialogs

        
@entrypoint
def remove_boards():    
    'remove boards by GUI'
#    
    board_names = boards().keys()
    sel=psidialogs.multi_choice(board_names, 
                            'select boards to remove from %s!' % boards_txt(), 
                            title='remove boards')

    for x in sel:
        remove_board(x)
        print x+' was removed'