def tamaño(n):
    return len(str(n))

def multClásica(u, v):
    return u * v

def mult(u, v):
    n = max(tamaño(u), tamaño(v))
    
    # Caso base: si los números son pequeños, usar multiplicación clásica
    if n <= 1:  # puedes ajustar este umbral según el caso
        return multClásica(u, v)
    else:
        s = n // 2
        
        # División de los números en mitades
        w = u // 10**s
        x = u % 10**s
        y = v // 10**s
        z = v % 10**s

        # Aplicación del algoritmo de Karatsuba
        parte1 = mult(w, y) * 10**(2 * s)
        parte2 = (mult(w + x, y + z) - mult(w, y) - mult(x, z)) * 10**s
        parte3 = mult(x, z)

        return parte1 + parte2 + parte3

u = int(input("Numero 1: "))
v = int(input("Numero 2: "))

resultado = mult(u, v)
print(f"El resultado es: {resultado}")