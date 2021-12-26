from bibliotecas import *

parser = argparse.ArgumentParser(description = 'Tarea 3 IA.')
parser.add_argument('algorithm', help = 'Metodo de Optimizacion')
args = parser.parse_args()
if args.algorithm == 'minimax':
    from methods.Minimax import minimaxRoot as method
elif args.algorithm == 'alphabeta':
    from methods.AlphaBetaPruning import minimaxRoot as method

def main():
    board = chess.Board()
    n = 0
    print(board)
    while n < 100:
        if n % 2 == 0: # Turno del jugador
            move = input("Ingrese un movimiento: ")
            move = chess.Move.from_uci(str(move))
            board.push(move)
        else: # Turno de la máquina
            print("Movimiento del oponente: ")
            move = method(3,board,True)
            move = chess.Move.from_uci(str(move))
            board.push(move)
        print(board)
        n += 1

if __name__ == "__main__":
    main()