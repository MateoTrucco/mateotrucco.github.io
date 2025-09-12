def ultimo_digito(x):
    return x % 10

def contar_digitos(x):
    return len(str(x))

def contar_pares_impares(x):
    pares, impares = 0, 0
    for digito in str(x):
        if int(digito) % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def suma_digitos(x):
    return sum(int(digito) for digito in str(x))

# Ejemplo de uso
x = int(input("Ingrese un número natural: "))
print(f"Último dígito: {ultimo_digito(x)}")
print(f"Cantidad de dígitos: {contar_digitos(x)}")
pares, impares = contar_pares_impares(x)
print(f"Cantidad de dígitos pares: {pares}, impares: {impares}")
print(f"Suma de los dígitos: {suma_digitos(x)}")
