from .circulo import perimetro_circulo
from .cuadrado import perimetro_cuadrado
from .poligono import perimetro_poligono
from .triangulo import perimetro_triangulo
from utils import clear_screen
from utils import pause



def mostrar_menu_perimetros():
    clear_screen()
    while True:
        print("\n--- Menú de Perímetros ---")
        print("1. Cuadrado")
        print("2. Triángulo")
        print("3. Polígono Regular")
        print("4. Círculo")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una figura: ")

        if opcion == '1':
            clear_screen()
            try:
                lado = float(input("Ingrese la longitud del lado del cuadrado: "))
                perimetro = perimetro_cuadrado(lado)
                print(f"El perímetro del cuadrado es: {perimetro}")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
            pause()
        elif opcion == '2':
            clear_screen()
            try:
                lado1 = float(input("Ingrese la longitud del lado 1 del triángulo: "))
                lado2 = float(input("Ingrese la longitud del lado 2 del triángulo: "))
                lado3 = float(input("Ingrese la longitud del lado 3 del triángulo: "))
                perimetro = perimetro_triangulo(lado1, lado2, lado3)
                print(f"El perímetro del triángulo es: {perimetro}")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
            pause()
        elif opcion == '3':
            clear_screen()
            try:
                num_lados = int(input("Ingrese el número de lados del polígono: "))
                longitud_lado = float(input("Ingrese la longitud de un lado del polígono: "))
                perimetro = perimetro_poligono(num_lados, longitud_lado)
                print(f"El perímetro del polígono regular es: {perimetro}")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")
            pause()
        elif opcion == '4':
            clear_screen()
            try:
                radio = float(input("Ingrese el radio del círculo: "))
                perimetro = perimetro_circulo(radio)
                print(f"El perímetro del círculo es: {perimetro}")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
            pause()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

