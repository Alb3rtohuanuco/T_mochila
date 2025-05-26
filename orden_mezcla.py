def met_mergesort(arr):
    if len(arr) <=1:
        return arr
    
    mid = len(arr) // 2
    izq = arr[:mid]
    der = arr[mid:]

    izq = met_mergesort(izq)
    der = met_mergesort(der)

    return met_merge(izq, der)

def met_merge(a, b):
    c = []
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    while i < len(a):
        c.append(a[i])
        i += 1

    while j < len(b):
        c.append(b[j])
        j += 1
    return c

lista1 = [1, 7, 3, 8, 4]

z = met_mergesort(lista1)
print(f"La lista ordenada: {z}")