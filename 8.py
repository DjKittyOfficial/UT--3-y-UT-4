try:
    n = int(input("Introduce un número: "))
    print("El doble es: {n*2}")
except:
    print("Error: no es un número")
else:
    print("Todo bien!")
finally:
    print("Programa terminado")
