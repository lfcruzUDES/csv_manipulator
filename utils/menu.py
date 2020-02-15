"""This a menu of the program."""


def instructions():
    """Muestra las instrucciones del programa."""
    print(
        """
        ---------------------------
        UDES Tools: manipulador CSV
        ---------------------------

    1. Ingresa la ruta del archivo.
    2. Ingresa el nombre del archivo.
    3. Se te mostrarán las columnas disponibles:
        - Para seleccionar las columnas a extraer usa el número de la
        columna y separa las columnas por comas: 1, 2, 3, 20. El orden
        en que coloques los números será el orden en que se mostrará
        las columnas en el archivo final.
        - Para unir colmnas usa el signo '-': 1-3.
    4. Se te pedirá el tipo de formato a aplicar en cada celda:
        - u: mayúsculas.
        - l: minúsculas.
        - lu: mayúsculas y minúsculas.
        Ejemplo: u, lu, l -> Esto indica que la celda 1 de cada
        fila deberá ser transformada a mayúsculas, la celda 2
        amayúsculas y minúsculas y la celda 3 a minúsculas.
        """
    )
