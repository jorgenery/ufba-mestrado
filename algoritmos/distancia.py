def calcular_distancia(rota, distancias):
    return (
        sum(distancias[rota[i]][rota[i + 1]] for i in range(len(rota) - 1))
        + distancias[rota[-1]][rota[0]]
    )
