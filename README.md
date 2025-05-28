# 🚀 Optimización de Delivery con Algoritmos de Ordenamiento y Búsqueda

**Proyecto UTN Programacion 2025** que implementa QuickSort, Merge Sort y Búsqueda Binaria para optimizar rutas de delivery, validando su eficiencia con datos simulados.

## 📂 Estructura del Proyecto


## 🛠️ Requisitos

- Python 3.10+
- Librerías:
  ```bash
  pip install matplotlib

▶️ Ejecución

Generar datasets (opcional):

bash
python generar_datos.py  # Crea archivos en /data/
Ejecutar análisis principal:

bash
python main.py
Resultados:

Gráficos guardados en /results/

Salida en consola:

=== Resultados ===
- Búsqueda binaria: Pedido en zona B10 encontrado en índice 427 (13 comparaciones)
- Tiempos de ordenamiento:
  100 pedidos: QuickSort=0.0023s | MergeSort=0.0031s
  1000 pedidos: QuickSort=0.0256s | MergeSort=0.0302s
  10000 pedidos: QuickSort=0.3120s | MergeSort=0.2945s

📊 Métricas Analizadas

Algoritmo	Complejidad	Estabilidad	Mejor caso
QuickSort	O(n log n)	No	Datos aleatorios
MergeSort	O(n log n)	Sí	Datos parcialmente ordenados
Búsq. Binaria	O(log n)	-	Listas ordenadas

📝 Notas

Los datasets simulados incluyen: id, distancia, zona, hora y prioridad.

Para personalizar pruebas, modificar archivos en main.py.

### Características clave:
1. **Modular**: Fácil extensión para nuevos algoritmos.
2. **Validado**: Pruebas con datasets de 100 a 10k pedidos.
3. **Visual**: Gráficos automáticos con matplotlib.
4. **Documentado**: Explicaciones teóricas y técnicas integradas.
