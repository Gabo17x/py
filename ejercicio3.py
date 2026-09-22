def medalla(nota):
    if nota > 4.5:
        return "Oro"
    elif nota >= 4.0:
        return "Plata"
    elif nota >= 3.8:
        return "Bronce"
    else:
        return "Sin Medalla"

# ciclo para usarlo
for i in range(3):
    nota = float(input("Nota: "))
    print(medalla(nota))