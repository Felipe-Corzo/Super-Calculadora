from pi import calcular_pi
from factorial import calcular_factorial
from fibonacci import calcular_fibonacci
from numeros_amigos import calcular_numeros_amigos
from numeros_perfectos import calcular_numeros_perfectos

def mostrar_submenu():
    
    print("\n=== Análisis Numérico ===")
    print("1. Cálculo de Pi")
    print("2. Cálculo de Factorial")
    print("3. Secuencia de Fibonacci")
    print("4. Números Amigos")
    print("5. Números Perfectos")
    print("6. Volver al menú principal")
    return input("Seleccione una opción (1-6): ")


def ejecutar_analisis():
    
    while True:
        opcion = mostrar_submenu()

        if opcion == "1":
            print(f"Valor aproximado de Pi: {calcular_pi()}")
        elif opcion == "2":
            n = int(input("Ingrese un número para calcular su factorial: "))
            print(f"Factorial de {n}: {calcular_factorial(n)}")
        elif opcion == "3":
            n = int(input("Ingrese cuántos términos de Fibonacci desea ver: "))
            print(f"Secuencia de Fibonacci: {calcular_fibonacci(n)}")
        elif opcion == "4":
            print(f"Números amigos encontrados: {calcular_numeros_amigos()}")
        elif opcion == "5":
            print(f"Números perfectos encontrados: {calcular_numeros_perfectos()}")
        elif opcion == "6":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
            
ejecutar_analisis()
