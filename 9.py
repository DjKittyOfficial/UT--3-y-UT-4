contador = 5

while contador > 0:
    print("Valor:", contador)
    contador = contador - 1
    if contador == 2:
        print("Salto el 2")
        continue
print("Fin del bucle")
