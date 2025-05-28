def quicksort(pedidos, clave="distancia"):
    """Ordena pedidos usando QuickSort (in-place)."""
    if len(pedidos) <= 1:
        return pedidos
    pivot = pedidos[len(pedidos)//2][clave]
    menores = [p for p in pedidos if p[clave] < pivot]
    iguales = [p for p in pedidos if p[clave] == pivot]
    mayores = [p for p in pedidos if p[clave] > pivot]
    return quicksort(menores, clave) + iguales + quicksort(mayores, clave)

def mergesort(pedidos, clave="hora"):
    """Ordena pedidos usando Merge Sort (estable)."""
    if len(pedidos) <= 1:
        return pedidos
    mitad = len(pedidos) // 2
    izquierda = mergesort(pedidos[:mitad], clave)
    derecha = mergesort(pedidos[mitad:], clave)
    return _merge(izquierda, derecha, clave)

def _merge(izq, der, clave):
    """Fusión de listas ordenadas."""
    resultado = []
    i = j = 0
    while i < len(izq) and j < len(der):
        if izq[i][clave] <= der[j][clave]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado