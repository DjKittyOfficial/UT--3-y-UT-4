def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
n = int(input("Introduce un número para verificar si es primo: "))
if es_primo(n):
    print(f"{n} es un número primo.")
else:
    print(f"{n} no es un número primo.")    