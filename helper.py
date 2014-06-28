import TTTBoard
import random

MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player

EMPTY = TTTBoard.EMPTY
X = TTTBoard.X
O = TTTBoard.O

def switch_player(player):
    if player == X:
        return O
    else:
        return X

def mc_trial(board, player):
    """
    fills the board
    until the game 
    is finished
    """
    empty = board.get_empty_squares()
    leng = len(empty)
    while True:
        box = random.randrange(leng)
        row = empty[box][0]
        col = empty[box][1]
        board.move(player, row, col)
        result = board.check_win()
        if result != None:
            return 
        del empty[box]
        leng -= 1
        player = switch_player(player)

def mc_update_scores(scores, board, player):
    """
    updates the scores
    after a game is finished
    """
    result = board.check_win()
    other = switch_player(player)
    if result != player and result != other:
        return
    dim = board.get_dim()
    other = switch_player(result)
    for cou1 in range(dim):
        for cou2 in range(dim):
            status = board.square(cou1, cou2)
            if status == result:
                if result == player:
                    scores[cou1][cou2] += MCMATCH
                else:
                    scores[cou1][cou2] += MCOTHER
            elif status == other:
                if result == player:
                    scores[cou1][cou2] -= MCMATCH
                else:
                    scores[cou1][cou2] -= MCOTHER

def get_best_move(board, scores):
    """
    returns the best
    possible move from the available
    moves
    """
    best = []
    empty = board.get_empty_squares()
    maxi = float('-inf')
    for squ in empty:
        score = scores[squ[0]][squ[1]]
        if score > maxi:
            best = []
            best.append(squ)
            maxi = score
        elif score == maxi:
            best.append(squ)
    index = random.randrange(len(best))
    return best[index]

def mc_move(board, player, trials):
    """
    returns the best possible move
    """
    dim = board.get_dim()
    scores = [ [0 for dummy_cou in range(dim)] for dummy_cou2 in range(dim)] 
    for dummy_cou in range(trials):
        copy_board = board.clone()
        mc_trial(copy_board, player)
        mc_update_scores(scores, copy_board, player)
    return get_best_move(board, scores)

def play_terminal(dim, mc_move, trials):
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
            if board.square(orow, ocol) == EMPTY:
                break
            print ''
        board.move(other, orow, ocol)

def format_result(board, player):
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
