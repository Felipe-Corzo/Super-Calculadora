from .circulo import area_circulo
from .cuadrado import area_cuadrado
from .poligono import area_poligono
from .triangulo import area_triangulo
from utils import clear_screen
from utils import pause
def menu_areas():
    while True:
        clear_screen()
        print("\nCalculadora de Áreas")
        print("1. Área del Cuadrado.")
        print("2. Área del Polígono Regular.")
        print("3. Área del Triángulo.")
        print("4. Área del Circulo.")
        print("5. Salir.")
        opcion = input("Selecciona una opción (1-5): ")
        try:
            if opcion == '1':
                clear_screen()
                lado = float(input("Ingresa la longitud del lado del cuadrado: "))
                area_cuadrado(lado)
                pause()
            elif opcion == '2':
                clear_screen()
                n_lados = int(input("Ingresa el número de lados del polígono (mínimo 3): "))
                lado = float(input("Ingresa la longitud del lado del polígono: "))
                area_poligono(n_lados, lado)
                pause()
            elif opcion == '3':
                clear_screen()
                base = float(input("Ingresa la base del triángulo: "))
                altura = float(input("Ingresa la altura del triángulo: "))
                area_triangulo(base, altura)
                pause()
            elif opcion == '4': 
                clear_screen()
                radio=float(input("Ingrese el radio del circulo: "))
                area_circulo(radio)
                pause()
            elif opcion == '5':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")

        except ValueError as e:
            print(f"Error: {e}")

