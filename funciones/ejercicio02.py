def es_valida(contrasena):
    return len(contrasena) >= 8

print(es_valida("secreta123"))
print(es_valida("secreta"))
print(es_valida("12345678"))
print(es_valida("hola"))
