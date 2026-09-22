"""Devuelve cuánto se debe pagar de propina según el porcentaje indicado."""
def calcular_propina(cuenta, porcentaje=10):

    
    # 'porcentaje=10' es un valor por defecto: si no se especifica, se usa 10%
    # Se divide el porcentaje entre 100 para convertirlo en proporción (ej: 10 -> 0.10)
    # y se multiplica por el valor de la cuenta para obtener el monto de la propina
    return cuenta * (porcentaje / 100)