from bibliotecas import *
from evaluation.evaluate import evaluate_board

def alphaBetaAlgorithm(depth, board, isMaximizing):
    '''
    Calcula la mejor jugada y el puntaje asociado a ella a partir del tablero con cierta profundidad

    Parameters
    ----------
    depth : int
        Profundidad a explorar la jugada
    board : chess.Board
        Tablero que contiene la posicion actual
    isMaximizing : bool
        Booleano que permite al agente saber si debe maximizar o minimizar segun sea su turno o no.

    Return
    ------
    bestMoveFinal : chess.Move
        Retorna la jugada a realizar
    '''
    possibleMoves = board.legal_moves
    bestMove = -9999
    bestMoveFinal = None
    for x in possibleMoves:                                                                 # Recorre todos los posibles movimientos que se pueden realizar
        move = chess.Move.from_uci(str(x))                                                  # Se convierte el movimiento al formato adecuado
        board.push(move)                                                                    # Se realiza el movimiento en el tablero
        value = max(bestMove, minimax(depth - 1, board, -10000, 10000, not isMaximizing))
        board.pop()                                                                         # Restaura la posicion anterior y devuelve la ultima jugada del stack
        # Actualizamos los valores de bestMove y el movimiento para ir guardando la mejor jugada
        if(value > bestMove):
            # print("Best score: " ,str(bestMove))
            # print("Best move: ",str(bestMoveFinal))
            bestMove = value
            bestMoveFinal = move
    return bestMoveFinal



def minimax(depth, board, alpha, beta, is_maximizing):
    '''
    Calcula la evaluacion de la posicion en el tablero una vez calculadas n jugadas.

    Parameters
    ----------
    depth : int
        Profundidad a explorar la jugada
    board : chess.Board
        Tablero que contiene la posicion actual
    alpha : float
    beta : float
    isMaximizing : bool
        Booleano que permite al agente saber si debe maximizar o minimizar segun sea su turno o no.

    Return
    ------
    bestMove : chess.Move
        Retorna la evaluacion de la mejor jugada
    '''
    # Una vez que llegamos a la profundidad deseada, evaluamos la posicion del tablero
    # De forma de elegir asi la mejor evaluacion una vez calculadas las depth jugadas.
    if(depth == 0):
        return -evaluate_board(board)

    possibleMoves = board.legal_moves
    if(is_maximizing):                          # Simula el turno de la máquina, por lo que se maximiza la recompensa
        bestMove = -9999
        for x in possibleMoves:                 # Recorre todos los posibles movimientos que se pueden realizar
            move = chess.Move.from_uci(str(x))  # Se convierte el movimiento al formato adecuado
            board.push(move)                    # Se realiza el movimiento en el tablero
            bestMove = max(bestMove,minimax(depth - 1, board, alpha, beta, not is_maximizing))
            board.pop()                         # Restaura la posicion anterior y devuelve la ultima jugada del stack
            alpha = max(alpha, bestMove)        # Se actualiza el valor de alpha, ya que es el turno del agente
            if beta <= alpha:
                return bestMove
        return bestMove
    else:                                       # Simula el turno del usuario, por lo que la máquina tiene que minimizar la recompensa del oponente
        bestMove = 9999
        for x in possibleMoves:                 # Recorre todos los posibles movimientos que se pueden realizar
            move = chess.Move.from_uci(str(x))  # Se convierte el movimiento al formato adecuado
            board.push(move)                    # Se realiza el movimiento en el tablero
            bestMove = min(bestMove, minimax(depth - 1, board,alpha,beta, not is_maximizing))
            board.pop()                         # Restaura la posicion anterior y devuelve la ultima jugada del stack
            beta = min(beta, bestMove)          # Se actualiza el valor de beta, ya que es el turno del oponente
            if(beta <= alpha):
                return bestMove
        return bestMove