def vizinho_mais_proximo(
    matriz_distancias, cidade_inicial=0, distancia_maxima=float("inf")
):
    n = len(matriz_distancias)
    visitadas = [False] * n
    rota = [cidade_inicial]
    distancia_total = 0

    cidade_atual = cidade_inicial
    visitadas[cidade_atual] = True

    for _ in range(n - 1):
        # Encontra a próxima cidade com a menor distância, não visitada
        proxima_cidade = np.argmin(
            [
                matriz_distancias[cidade_atual][j] if not visitadas[j] else float("inf")
                for j in range(n)
            ]
        )
        distancia_para_proxima = matriz_distancias[cidade_atual][proxima_cidade]

        # Verifica se adicionar a próxima cidade excede a distância máxima
        if distancia_total + distancia_para_proxima > distancia_maxima:
            return None, None

        distancia_total += distancia_para_proxima
        rota.append(proxima_cidade)
        visitadas[proxima_cidade] = True
        cidade_atual = proxima_cidade

    # Adiciona a distância de volta para a cidade inicial
    distancia_final = matriz_distancias[cidade_atual][cidade_inicial]

    if distancia_total + distancia_final > distancia_maxima:
        return None, None

    distancia_total += distancia_final
    rota.append(cidade_inicial)

    return rota, distancia_total
