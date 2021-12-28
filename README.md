# Proyecto de Aprendizaje
## Seminario II - Inteligencia Artificial en Agentes Autónomos
### Autor    :  Daniel Espinoza / Ian Roberts / Juan Pablo Sánchez / Jorge Veliz
### Profesor : Mauricio Araya 

El enfoque de esta tarea involucra la comparación de métodos de búsqueda y decisión en teoría de juegos, como son **minimax** y **alphabeta**, aplicados al juego de ajedrez.
# Tabla de Contenidos
1. [Objetivos](#id0)
2. [Instalación](#id1)
3. [Descripción del problema](#id2)
4. [Algoritmos de aprendizaje](#id3)
    * [Minimax](#id3.1) 
    * [Alphabeta](#id3.2)
5. [Resultados](#id4)

# Objetivos <div id="id0"></div>
# Instalación <div id="id1"></div>

El proyecto utiliza Python en una versión superior a 3.0. Esta implementación en particular fue desarrollada en Python 3.8.10 utilizano la biblioteca `python-chess`.

1. Instalar dependencias de `python-chess`.
~~~~
pip install python-chess
~~~~

2. Clonar el repositorio.
~~~~
git clone git@github.com:D-Cryp7/T3-TEL352.git
~~~~

3. Iniciar el programa para ejecutar ajedrez con el método `minimax`.
~~~~
python3 main.py minimax
~~~~

4. Iniciar el programa para ejecutar ajedrez con el método `alphabeta`.
~~~~
python3 main.py alphabeta
~~~~

# Descripción del problema <div id="id2"></div>

Se plantea una implementación basada en el juego de ajedrez. Este es un juego de tablero donde participan dos jugadores que se enfrentan entre sí, cada uno dispone al comienzo del juego 16 piezas móviles que son ubicadas en posiciones determinadas sobre un tablero de dimensiones 8x8.

Este es un juego de estrategia donde cada jugador busca *derrocar* al rey oponente amenazando con las piezas de modo que este sea incapaz de moverse a posiciones seguras mientras se protegue al rey propio. Esta situación donde el rey no tiene movimientos  

<p align="center">
 <img src="sample/chess-board-illustration.webp" title=""/><figcaption align="center">Diagrama del tablero y piezas de ajedrez</figcaption>
</p>

El tablero consiste de un cuadrado de dimensiones 8x8 donde se tienen en total 64 casillas de colores blanco y negro intercaladas entre si. Las filas del tablero son identificadas con números mientras que las columnas con letras de modo que cada casilla puede ser identificada con con un par coordenado de letra y número (Por ejemplo casilla B4, casilla G8, etc.) 

Además cada jugador cuenta con un set de 16 piezas ubicadas al comienzo del juego en los extremos del tablero como se muestra en la imagen anterior. Las piezas se componen de 8 peones, 2 torres, 2 caballos, 2 alfiles, el rey y la reina, cada uno con sus mécanicas propias.

- Peón : Pieza básica identificada con una (P o p). Esta pieza se mueve verticalmente por la columna en la que se encuentra y es incapaz de retroceder. Puede capturar o *comer* otra pieza moviendose en diagonal 1 espacio hacia al frente.   
- Torre : Pieza identificada con una (R o r) en el tablero. Esta pieza es capaz de en linea recta por la columna o la fila en la que se encuentre sin poder pasar por otra pieza en su camino a menos que busque capturarla.
- Caballo : Pieza identificada con una (N o n) en el tablero. Este posee un movimiento especial en forma de L y a diferencia de otras piezas puede saltar por piezas intermedias para llegar a su destino. 
- Alfín : Pieza identificada con una (B o b) en el tablero. El alfín es capaz de de forma similar a la torre solo que en sentido diagonal.

- Reina : Pieza identificada con una (Q o q) en el tablero. La reina tiene la mayor movilidad dentro del juego ya que puede desplazarse en todo sentido integrando el desplazamiento del alfín y la torre en una sola pieza.

- Rey : Pieza identificada con una (K o k) en el tablero. El rey por último, es la pieza más importante del juego y puede desplazarse en todo sentido como la reina pero solo una cuadrícula a la vez.

## Movimientos y coordenadas


# Algoritmos de aprendizaje <div id="id3"></div>
# Algoritmo Minimax <div id="id3.1"></div>
# Algoritmo Alphabeta <div id="id3.2"></div>
# Resultados <div id="id4"></div>
