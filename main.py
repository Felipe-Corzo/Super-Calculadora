from areas import menu_areas
from perimetro import mostrar_menu_perimetros
from utils import clear_screen
def mostrar_menu_principal():
    print("\n===== CALCULADORA MATEMÁTICA =====")
    print("1. Cálculo de Áreas")
    print("2. Cálculo de Perimetros")
    print("3. Análisis numérico")
    print("4. Salir")
    return input("Seleccione una opción (1-4): ")
def main():
    clear_screen()
    while True:
        clear_screen()
        opcion = mostrar_menu_principal()
        if opcion == "1":
            menu_areas()
        elif opcion == "2":
            mostrar_menu_perimetros()
        elif opcion == "3":
            print("Módulo de Análisis numérico")
        elif opcion == "4":
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()

