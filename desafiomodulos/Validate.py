

def validate_number() -> int:
    """Valida que un numero sea entero

    Returns:
        int: retorna un numero entero
    """
    opcion = ""

    while opcion == "" or not opcion.isnumeric():
        opcion = input(f'Escriba en numero entero: ')

    return int(opcion)


def validate_length(mensaje:str):
    """Valida longitud del texto ingresado

    Args:
        mensaje (str): se ingresa el mensaje para saber su longitud

    Returns:
        bool: retorna un valor booleano
    """
    opcion = ""

    if opcion == "" and len(mensaje) > 0:
        return True
    else:
        return False
    


