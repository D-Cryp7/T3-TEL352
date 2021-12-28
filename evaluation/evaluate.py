from bibliotecas import *

def evaluate_board(board, time_limit = 0.01):
    '''
    Funcion que permite evaluar la posicion que se encuentra en el tablero actualmente, desde el punto de vista de las piezas Blancas
    
    Parameters
    ----------
    board : chess.Board
        Tablero que contiene la posicion actual
    time_limit : float
        Cantidad de tiempo que tiene el engine para evaluar la posicion

    Returns
    -------
    evaluation : int
        Entero que entrega el valor numerico de la posicion actual en CentiPawns
    '''
    evaluation = 0
    engine = chess.engine.SimpleEngine.popen_uci(r"E:/Downloads/T3-TEL352/stockfish_10_x64.exe")    # Cargamos StockFish para evaluar la posicion
    result = engine.analyse(board, chess.engine.Limit(time = time_limit))                           # Obtenemos la evaluacion de StockFish para la posicion
    # Si es que la jugada es un Mate debemos asignarle nosotros un valor, que sera de 9999.
    if result['score'].is_mate():
        evaluation = 9999
    else:
        evaluation = result['score'].white().score()                                                # Transformamos la evaluacion a entero
    engine.quit()
    return evaluation