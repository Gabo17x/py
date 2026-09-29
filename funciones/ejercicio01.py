def calcular_propina(cuenta, porcentaje=10):
    return cuenta * porcentaje / 100

print(calcular_propina(50000))
print(calcular_propina(50000, 15))
print(calcular_propina(120000, 20))
