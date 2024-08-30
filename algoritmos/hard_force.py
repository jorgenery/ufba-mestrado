from itertools import permutations


def calcular_distancia(rota, distancias):
    return (
        sum(distancias[rota[i]][rota[i + 1]] for i in range(len(rota) - 1))
        + distancias[rota[-1]][rota[0]]
    )


def forca_bruta(distancias, distancia_maxima):
    cidades = list(range(len(distancias)))
    melhor_rota = None
    menor_distancia = float("inf")

    for rota in permutations(cidades):
        distancia_atual = calcular_distancia(rota, distancias)
        if distancia_atual <= distancia_maxima and distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhor_rota = rota

    return melhor_rota, menor_distancia if melhor_rota else None
