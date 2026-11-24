# Problema 1: Nivel de Compromiso de Sesiones de Clientes

# 1. Definir la matriz con al menos 5 sesiones
# Formato por fila: [ID del Cliente, Duración en segundos, Número de clics]
matriz_sesiones = [
    [101, 200, 10],
    [102, 45, 2],
    [103, 90, 5],
    [104, 185, 9],
    [105, 120, 4]
]

# 2. Función para clasificar el nivel de compromiso
def clasificarCompromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

# 3. Recorrer la matriz y mostrar resultados
print("=" * 40)
print("   INFORME DE COMPROMISO DE CLIENTES")
print("=" * 40)
print(f"{'ID Cliente':<12} {'Clasificación':<15}")
print("-" * 40)

for sesion in matriz_sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]
    nivel = clasificarCompromiso(duracion, clics)
    print(f"{id_cliente:<12} {nivel:<15}")

print("=" * 40)
print("Programa finalizado.")
