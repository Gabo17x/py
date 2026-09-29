correos = ["ana@gmail.com", "luis", "carlos@hotmail.com", "sena"]

validos = [correo for correo in correos if "@" in correo]

print(validos)
