from .circulo import area_circulo
from .cuadrado import area_cuadrado
from .poligono import area_poligono
from .triangulo import area_triangulo

def menu_areas():
    while True:
        print("\nCalculadora de Áreas")
        print("1. Área del Cuadrado")
        print("2. Área del Polígono Regular")
        print("3. Área del Triángulo")
        print("4. Salir")
        opcion = input("Selecciona una opción (1-4): ")
        try:
            if opcion == '1':
                lado = float(input("Ingresa la longitud del lado del cuadrado: "))
                area_cuadrado(lado)
            elif opcion == '2':
                n_lados = int(input("Ingresa el número de lados del polígono (mínimo 3): "))
                lado = float(input("Ingresa la longitud del lado del polígono: "))
                area_poligono(n_lados, lado)
            elif opcion == '3':
                base = float(input("Ingresa la base del triángulo: "))
                altura = float(input("Ingresa la altura del triángulo: "))
                area_triangulo(base, altura)
            elif opcion == '4':
                print("Saliendo...")
                break
            else:
                print("Opción no válida, intenta de nuevo.")

        except ValueError as e:
            print(f"Error: {e}")

