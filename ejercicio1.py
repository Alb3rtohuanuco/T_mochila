def tamaño(n):
    return len(str(n))

def multClásica(u, v):
    return u * v

def mult(u, v):
    if u == 0 or v == 0:
        return 0

    n = max(tamaño(u), tamaño(v))

    if n <= 1:
        return multClásica(u, v)
    else:
        s = n // 2

        w = u // (10 ** s)
        x = u % (10 ** s)
        y = v // (10 ** s)
        z = v % (10 ** s)

        parte1 = mult(w, y) * (10 ** (2 * s))
        parte2 = (mult(w, z) + mult(x, y)) * (10 ** s)
        parte3 = mult(x, z)

        return parte1 + parte2 + parte3

# Entrada del usuario
try:
    u = int(input("Ingresa el primer número: "))
    v = int(input("Ingresa el segundo número: "))
    resultado = mult(u, v)
    print("Resultado:", resultado)
except ValueError:
    print("Por favor, ingresa solo números enteros válidos.")