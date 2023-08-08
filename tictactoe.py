"""
Tic Tac Toe Player
"""

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    return O if x_count > o_count else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise ValueError("Invalid action.")
    new_board = [row[:] for row in board]
    i, j = action
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        # Check rows
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        # Check columns
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board, alpha=float("-inf"), beta=float("inf"), maximizing=True):
    if terminal(board):
        return None, utility(board)

    if maximizing:
        maxEval = float('-inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            _, evaluation = minimax(new_board, alpha, beta, False)
            
            if evaluation > maxEval:
                maxEval = evaluation
                best_move = action
            
            alpha = max(alpha, evaluation)
            if alpha >= beta:
                break
        return best_move, maxEval

    else:
        minEval = float('inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            _, evaluation = minimax(new_board, alpha, beta, True)

            if evaluation < minEval:
                minEval = evaluation
                best_move = action
            
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return best_move, minEval