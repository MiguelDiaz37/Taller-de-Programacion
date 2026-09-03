"●"

def ingresar_dimensiones(pregunta1):
    while True:
        entrada = input(pregunta1)
        if entrada.isdigit() and int(entrada) >= 8:
            return int(entrada)
        else:
            print("Ingrese un numero entero mayor o igual a 8")

def iniciar_cuadricula(ancho,alto):
    return [['[○]' for _ in range(ancho)] for _ in range (alto)]

def validar (x, y, ancho, alto):
    return 1 <= x <= ancho and 1 <= y <= alto

def rellenar(cuadricula, x, y):
    fila = y - 1
    columna = x - 1 
    cuadricula[fila][columna] = '[●]'

def imprimir_cuadricula(cuadricula):
    for fila in cuadricula:
        print(' '.join(fila))


ancho = ingresar_dimensiones("Ingrese el ancho de la cuadricula X: ")
alto = ingresar_dimensiones("Ingrese el alto de la cuadricula Y: ")
cuadricula = iniciar_cuadricula(ancho,alto)
seleccionadas = []
imprimir_cuadricula(cuadricula)

while True:
    print("1. Seleccionar coordenada")
    print("2. Ver cuadricula")
    print("3. Ver seleccionadas")
    print("4. Reiniciar selecciones")
    print("5. Salir")
    entrada_opcion = opcion = (input("Opcion: "))
    if entrada_opcion.isdigit():
        opcion = int(entrada_opcion)
    else:
        print("Opcion invalida")
        continue
    if opcion == 1:
        entrada_x = input("Ingrese X: ")
        entrada_y = input("Ingrese Y: ")
        if entrada_x.isdigit() and entrada_y.isdigit():
            x = int(entrada_x)
            y = int(entrada_y)
            if validar(x, y, ancho, alto):
                rellenar(cuadricula, x, y)
                seleccionadas.append(f"{x}, {y}")
            else:
                print("Coordenada inexistente")
        else:
            print("Se deben ingresar numeros enteros")

    elif opcion == 2:
        imprimir_cuadricula(cuadricula)
    elif opcion == 3:
        print(seleccionadas)
    elif opcion == 4:
        cuadricula = iniciar_cuadricula(ancho,alto)
        seleccionadas = []
    elif opcion == 5:
        break
    else:
        print("Opcion invalida")
