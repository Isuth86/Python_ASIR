# Ejercicio Tablero de Ajedrez con asteriscos.

def chessboard_pattern(rows=8, cols=8, block_size=3, symbol="*"):
    """
    Genera un tablero de ajedrez donde cada casilla es un bloque de block_size x block_size.
    Las casillas negras se llenan con 'symbol', las blancas con espacios.
    """
    for r in range(rows):
        for i in range(block_size):  # cada casilla ocupa block_size filas
            line_parts = []
            for c in range(cols):
                if (r + c) % 2 == 0:
                    line_parts.append(symbol * block_size)
                else:
                    line_parts.append(" " * block_size)
            print("".join(line_parts))  # separación entre casillas
        # no añadimos líneas en blanco, todo compacto


# Ejemplo: tablero 8x8 con bloques 3x3 de asteriscos
chessboard_pattern(rows=8, cols=8, block_size=3, symbol="*")
