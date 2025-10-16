def calcular_pi(terminos=1000000):
    
    pi = 0
    for i in range(terminos):
        pi += ((-1) ** i) / (2 * i + 1)
    return 4 * pi

