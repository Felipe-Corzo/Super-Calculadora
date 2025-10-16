import math

def area_poligono(n_lados, lado):
    if n_lados < 3:
        raise ValueError("El número de lados debe ser al menos 3.")
    if lado <= 0:
        raise ValueError("La longitud del lado debe ser mayor que cero.")
    area = (n_lados * lado ** 2) / (4 * math.tan(math.pi / n_lados))
    print(f"El área del polígono regular es: {area:.2f}")
