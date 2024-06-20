
#funcion que suma dos numeros
def suma(a, b):
    if a is None or b is None:   #si alguno de los valores es nulo
        return None
    try:
        return int(a) + int(b)   #intentar convertir los valores a enteros y sumarlos
    except ValueError:
        return None

#funcion que resta dos numeros
def resta(a, b):
    if a is None or b is None:  
        return None
    try:
        return int(a) - int(b)
    except ValueError:  
        return None


#funcion que calcula el cuadrado de un binomio de dos numeros
def cuadrado_binomio(a, b):
    if a is None or b is None:
        return None
    try:
        a = int(a)
        b = int(b)
        return a**2 + 2*a*b + b**2
    except ValueError:
        return None


