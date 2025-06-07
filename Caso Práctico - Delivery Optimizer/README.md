# 🚀 Optimización de Delivery con Algoritmos de Ordenamiento y Búsqueda

## Integrantes del grupo:

Ariel Grela | Matías Higa

Comisión: 3

## Objetivo: 

Implementación de QuickSort, Merge Sort y Búsqueda Binaria para optimizar rutas de delivery, validando su eficiencia con datos simulados.

## 🔴 Video de Youtube:

https://youtu.be/jS7W-lFHjM0


## 📂 Estructura del Proyecto

```markdown
📦Caso Practico - Delivery Optimizer/
├── 📂 data/ # Datasets de prueba
│ ├── 📄 pedidos_100.json # 100 pedidos
│ ├── 📄 pedidos_1k.json # 1,000 pedidos
│ └── 📄 pedidos_10k.json # 10,000 pedidos
│
├── 📂 modules/ # Lógica de algoritmos
│ ├── 📄 sorting.py # QuickSort + MergeSort
│ ├── 📄 search.py # Búsqueda binaria
│ └── 📄 validation.py # Validadores
│
├── 📂 results/ # Outputs visuales
│ ├── 📊 comparativa.png
│ └── 📈 comparativa_barras.png
│
├── 📄 main.py # Script principal
└── 📄 README.md # Documentación
```

## 🛠️ Requisitos

- Python 3.10+
- Librerías:
  ```bash
  pip install matplotlib

## ▶️ Ejecución

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
- Búsqueda binaria: Pedido en zona B10 encontrado en índice 2967 (6 comparaciones)
- Tiempos de ordenamiento:
    ```bash
  100 pedidos: QuickSort=0.0000s | MergeSort=0.0000s
  1000 pedidos: QuickSort=0.0030s | MergeSort=0.0100s
  10000 pedidos: QuickSort=0.0069s | MergeSort=0.0197s

## 📊 Métricas Analizadas
```markdown
Algoritmo	Complejidad	Estabilidad	Mejor caso
QuickSort	O(n log n)	No	Datos aleatorios
MergeSort	O(n log n)	Sí	Datos parcialmente ordenados
Búsq. Binaria	O(log n)	-	Listas ordenadas
```

## 📝 Notas

Los datasets simulados incluyen: id, distancia, zona, hora y prioridad.

Para personalizar pruebas, modificar archivos en main.py.

### Características clave:
1. **Modular**: Fácil extensión para nuevos algoritmos.
2. **Validado**: Pruebas con datasets de 100 a 10k pedidos.
3. **Visual**: Gráficos automáticos con matplotlib.
4. **Documentado**: Explicaciones teóricas y técnicas integradas.
