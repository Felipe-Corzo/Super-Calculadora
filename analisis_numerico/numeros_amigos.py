def suma_divisores(n):
    
    divisores = [i for i in range(1, n) if n % i == 0]
    return sum(divisores)

def calcular_numeros_amigos():
    
    limite = 10000
    amigos = []
    for i in range(2, limite):
        suma_i = suma_divisores(i)
        if suma_i != i and suma_divisores(suma_i) == i:
            amigos.append((i, suma_i))
    return amigos

