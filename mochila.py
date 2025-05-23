def cambiar_monto(monto, denominaciones, cantidades):
    resultado = []
    for i in range(len(denominaciones)):
        denom = denominaciones[i]
        cantidad_disponible = cantidades[i]

        usar = min(int(monto // denom), cantidad_disponible)
        if usar > 0:
            resultado.append((usar, denom))
            monto -= usar * denom
            monto = round(monto, 2)  
    if abs(monto) < 0.00001:
        return resultado
    else:
        return None  

denominaciones = [200, 100, 50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05]
cantidades =     [1,   1,   1,  1,  1, 1, 2, 2,  1,   2,   1,   1]  
monto = 179.45  

respuesta = cambiar_monto(monto, denominaciones, cantidades)

if respuesta:
    print("Respuesta:")
    for cant, denom in respuesta:
        print(f"{cant} de S/{denom}")
else:
    print("No se puede pagar el monto exacto con las denominaciones disponibles.")