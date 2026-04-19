import Validate 
def get_int(mensaje:str, mensaje_error:str , minimo:int , maximo:int , reintentos:int) -> int|None:
    """_summary_

    Args:
        mensaje (str): es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola
        mensaje_error (str):mensaje de error en el caso de que el dato ingresado sea invalido
        minimo (int):  valor mínimo admitido (inclusive)
        maximo (int): valor máximo admitido (inclusive)
        reintentos (int): cantidad de veces que se volverá a pedir el dato en caso de error.

    Returns:
        int|None: retorna valor nulo
    """

    print(mensaje)
    cantidad_de_intentos = 0
    
    while True:
        numero_ingresado = input("Ingrese un numero entero:")
        if Validate.validate_number(numero_ingresado):
            return int(numero_ingresado)
        else:
            print(mensaje_error)
            if cantidad_de_intentos < reintentos:
                cantidad_de_intentos += 1
            else: 
                return None
            
def get_string(mensaje: str, mensaje_error: str, longitud: int, reintentos: int):
    """_summary_

    Args:
        mensaje (str):es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola
        mensaje_error (str): mensaje de error en el caso de que el dato ingresado sea invalido
        longitud (int): longitud de la cadena ingresada dado el parámetro recibido
        reintentos (int): cantidad de veces que se volverá a pedir el dato en caso de error

    Returns:
        _type_: retorna valor nulo
    """
    
    print(mensaje)
    cantidad_de_intentos = 0

    while True:
        texto_ingresado = input("ingrese un texto por favor: ")
        if Validate.validate_length(texto_ingresado):
            return texto_ingresado
        else:
            print(mensaje_error)
            if cantidad_de_intentos < reintentos:
                cantidad_de_intentos += 1
            else: 
                return None 


        
            




        

        


