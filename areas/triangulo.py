def area_triangulo(base, altura):
    if base <= 0:
        raise ValueError("La base debe ser mayor que cero.")
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que cero.")
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area:.2f}")
