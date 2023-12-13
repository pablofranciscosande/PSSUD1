 #0, 1, 1, 2, 3, 5, 8, 13, 21, 34…

def fibonacci(n): ### creo función para generar secuencia de fibonacci
    fib_lista = [0, 1] ### creo lista con los dos primeros dígitos de la sucesión de fibonacci
    while len(fib_lista) < n: ### creo bucle, mientras n sea > que el tamaño de fib_lista se ejecutará el método append que defino dentro para añadir el siguiente miembro de la sucesión de fibonacci a la lista
        fib_lista.append(fib_lista[-1] + fib_lista[-2]) ### creo el método para añadir un nuevo elemento a la lista fib_lista que será el resultado de la suma del último (-1) y penúltimo (-2) elemento de la lista.
    return fib_lista ### la función devuelve la sucesion de fibonacci en función a n.


try: ### creo la parte del programa que interacciona con el usuario
    n = int(input("Cuantos miembros de la secuencia de Fibonacci quieres ver?: ")) ### Pido al usuario que introduzca el número de miembros que quiere ver de la sucesión de Fibonacci en pantalla.
    if n <= 0: ### si el usuario introduce un 0 se le pedirá que introduzca un número positivo.
        print("Por favor, introduce un número positivo.")
    else:
        resultado = fibonacci(n) ### creo el resultado con valor la función de la secuencia de fibonacci 
        print(f"Secuencia de Fibonacci hasta el miembro {n}: {resultado}") ### imprimo la secuencia de Fibonacci 

        posicion = int(input("Introduce el número de la posición del miembro que deseas ver: "))
        
        if posicion < 1 or posicion > n: 
            print(f"Posición inválida. Por favor, introduce un número entre 1 y {n}.")
        else:
            print(f"El valor del miembro en la posición {posicion} es: {resultado[posicion-1]}")

except ValueError:
    print("Por favor, introduce un número entero.")