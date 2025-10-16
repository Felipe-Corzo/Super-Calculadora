def suma_divisores(n):
    
    divisores = [i for i in range(1, n) if n % i == 0]
    return sum(divisores)

def calcular_numeros_perfectos(limite=10000):
    
    perfectos = []
    for i in range(2, limite):
        if suma_divisores(i) == i:
            perfectos.append(i)
    return perfectos

