import TTTBoard
from helper import switch_player

# Useful constants
EMPTY = TTTBoard.EMPTY
X = TTTBoard.X
O = TTTBoard.O

def play_terminal(dim, mc_move, trials):
    """
    Makes the game playable on a terminal
    """
    board = TTTBoard.TTTBoard(dim)
    while True:
        try:
            other = raw_input("You are O or X [O/X] --> ")
        except:
            return
        if other == X or other == O:
            break
    player = switch_player(other)
    while True:
        if format_result(board, player):
            return
        move = mc_move(board, player, trials)
        board.move(player, move[0], move[1])
        if format_result(board, player):
            return
        print board
        while True:
            try:
                orow = input("[row] --> ")
                ocol = input("[col] --> ")
            except:
                return
            if orow > -1 and orow < dim and ocol > -1 and ocol < dim and board.square(orow, ocol) == EMPTY:
                break
            print ''
        board.move(other, orow, ocol)

def format_result(board, player):
# prints the result and returns True if the game is over
# otherwise returns False
    result = board.check_win()
    if result != None:
        if result == EMPTY:
            print "\nIts a draw"
        elif result == player:
            print "\nMachine wins!"
        else:
            print "\nYou win!"
        print board
        return True
    return False

