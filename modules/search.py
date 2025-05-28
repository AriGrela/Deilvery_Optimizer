def busqueda_binaria(pedidos_ordenados, zona_objetivo):
    izquierda, derecha = 0, len(pedidos_ordenados) - 1
    comparaciones = 0  # Contador nuevo
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        comparaciones += 1  # Cada iteración es una comparación
        
        if pedidos_ordenados[medio]["zona"] == zona_objetivo:
            print(f"Búsqueda binaria realizó {comparaciones} comparaciones")
            return medio, comparaciones  # Devuelve ambos valores
        elif pedidos_ordenados[medio]["zona"] < zona_objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1, comparaciones  # Devuelve ambos valores incluso si no encuentra