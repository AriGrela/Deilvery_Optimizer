def validar_pedido(pedido):
    """Valida que un pedido tenga campos requeridos y valores positivos."""
    if not all(key in pedido for key in ["id", "distancia", "zona", "hora", "prioridad"]):
        raise ValueError("Faltan campos obligatorios en el pedido")
    if pedido["distancia"] <= 0:
        raise ValueError("La distancia debe ser positiva")
    if pedido["prioridad"] not in range(1, 6):
        raise ValueError("Prioridad debe ser entre 1 y 5")