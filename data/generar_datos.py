import json
import random
from datetime import datetime, timedelta

def generar_pedidos(n):
    zonas = [f"{chr(65+i)}{j:02d}" for i in range(5) for j in range(1, 21)]  # Ej: A01, B12
    return [
        {
            "id": i+1,
            "distancia": round(random.uniform(1.0, 20.0), 2),
            "zona": random.choice(zonas),
            "hora": (datetime.now() - timedelta(minutes=random.randint(0, 1440))).strftime("%H:%M"),
            "prioridad": random.randint(1, 5)  # 1 = máxima prioridad
        } for i in range(n)
    ]

# Generar los pedidos que quieras y los guarda +
with open("data/pedidos_10k.json", "w") as f:
    json.dump(generar_pedidos(10000), f, indent=4)

