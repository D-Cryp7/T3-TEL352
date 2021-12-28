from bibliotecas import *
from methods.AlphaBetaPruning import evaluate_board

# Argumentos por Consola
# Se definen los argumentos a recibir, en este caso es solamente el algoritmo a utilizar
# Posibles valores que se pueden entregar son:
# - minimax
# - alphabeta
parser = argparse.ArgumentParser(description = 'Tarea 3 IA.')
parser.add_argument('algorithm', help = 'Metodo de Optimizacion')
args = parser.parse_args()

# Cargamos el algoritmo requerido por el usuario
if args.algorithm == 'minimax':
    from methods.Minimax import minimaxAlgorithm as method
elif args.algorithm == 'alphabeta':
    from methods.AlphaBetaPruning import alphaBetaAlgorithm as method
else:
    print('[ERROR]: El argumento no es un algoritmo valido!')


def main():
    # Generamos el tablero
    board = chess.Board()
    print(board, '\n')
    #print('\n')
    n = 0       # Contador que controla si juega la máquina o el jugador
    # Jugamos hasta que haya un jaquemate en el tablero
    while not board.is_game_over():
        # Turno del jugador
        if n % 2 == 0:
            while True:
                move = input("Ingrese un movimiento: ")
                move = chess.Move.from_uci(str(move))
                # Verificamos que el movimiento sea legal
                if move in board.legal_moves:
                    board.push(move)
                    break
                else:
                    print("[ERROR]: Movimiento ilegal")
        # Turno de la máquina
        else: 
            start = time.time()
            move = method(depth = 2, board = board, isMaximizing = True)
            end = time.time()
            print("Movimiento del oponente: ", move, 'calculado en :', end-start, 'segundos.')
            move = chess.Move.from_uci(str(move))
            board.push(move)

        print()
        print(board, '\n')
        n += 1

def test():
    board = chess.Board("r1bqkbnr/pppppppp/2n5/8/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQk - 5 4")
    # Blancas mejor: rnbqkb1r/pppp1ppp/5n2/8/4Pp2/2N5/PPPP2PP/R1BQKBNR w KQkq - 0 4
    # Negras mejor: rnbqkb1r/pppp1ppp/5n2/8/3PPp2/8/PPP3PP/R1BQKBNR w KQkq - 1 6
    # Mate: r1bqkbnr/pppppppp/2n5/8/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQk - 5 4
    print(evaluate_board(board))

if __name__ == "__main__":
    main()