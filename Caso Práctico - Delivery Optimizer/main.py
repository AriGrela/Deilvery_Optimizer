import json
import time
import matplotlib.pyplot as plt
import os
import sys
from modules.sorting import quicksort, mergesort
from modules.search import busqueda_binaria
from modules.validation import validar_pedido

# 🔧 Asegurarse de que el directorio de trabajo sea donde está main.py
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Configuración
archivos = {
    100: "data/pedidos_100.json",
    1000: "data/pedidos_1k.json",
    10000: "data/pedidos_10k.json"
}
tamanios = sorted(archivos.keys())  # [100, 1000, 10000]

# Cargar y validar todos los datasets
datasets = {}
for n, archivo in archivos.items():
    with open(archivo) as f:
        datos = json.load(f)
    for pedido in datos:
        validar_pedido(pedido)
    datasets[n] = datos

# Medir tiempos de ordenamiento
resultados = {}
for algoritmo in [quicksort, mergesort]:
    tiempos = []
    for n in tamanios:
        datos = datasets[n].copy()  # Usamos copia para no modificar el original
        inicio = time.time()
        algoritmo(datos, "distancia" if algoritmo == quicksort else "hora")
        tiempos.append(time.time() - inicio)
    resultados[algoritmo.__name__] = tiempos

# Búsqueda binaria (usamos el dataset de 10k como ejemplo y cuenta cantidad de comparaciones.)
pedidos_por_zona = sorted(datasets[10000], key=lambda x: x["zona"])
indice, comparaciones = busqueda_binaria(pedidos_por_zona, "B10")

# Generar gráfico comparativo
plt.figure(figsize=(10, 5))
plt.plot(tamanios, resultados["quicksort"], marker="o", label="QuickSort (Distancia)")
plt.plot(tamanios, resultados["mergesort"], marker="s", label="Merge Sort (Hora)")
plt.xlabel("Número de pedidos")
plt.ylabel("Tiempo (segundos)")
plt.title("Comparación de algoritmos de ordenamiento")
plt.legend()
plt.grid()

# Guardar gráfico
plt.savefig("results/comparativa.png")
plt.close()  # Cierra la figura para liberar memoria

# Gráfico adicional: Tiempos promedio
plt.figure(figsize=(8, 4))
nombres = list(resultados.keys())
tiempos_promedio = [sum(t) / len(t) for t in resultados.values()]
plt.bar(nombres, tiempos_promedio, color=["skyblue", "salmon"])
plt.ylabel("Tiempo promedio (segundos)")
plt.title("Rendimiento promedio por algoritmo")
plt.savefig("results/comparativa_barras.png")

# Resultados en consola
print("\n=== Resultados ===")
print(f"- Búsqueda binaria: Pedido en zona B10 encontrado en índice {indice} ({comparaciones} comparaciones)")
print("- Tiempos de ordenamiento:")
for i, n in enumerate(tamanios):
    print(f"  {n} pedidos: QuickSort={resultados['quicksort'][i]:.4f}s | MergeSort={resultados['mergesort'][i]:.4f}s")
print("\n- Gráficos guardados en:")
print("  results/comparativa.png")
print("  results/comparativa_barras.png")