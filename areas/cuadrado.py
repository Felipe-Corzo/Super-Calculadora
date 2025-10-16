def area_cuadrado( lado):
        if lado < 0:
            raise ValueError("El lado no puede ser negativo.")
        area = lado **2
        print(f"El area del cuadrado es: {area:.2f}")
