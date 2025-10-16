def area_circulo (radio):
        if radio < 0:
                raise ValueError("El radio no puede ser negativo.")
        pi = 3.1416
        area = pi * radio**2
        print(f"El area de tu circulo es {area:.2f}")
