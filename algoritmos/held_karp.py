import itertools


def held_karp(distances, max_distance):
    n = len(distances)
    C = {}

    for k in range(1, n):
        C[(1 << k, k)] = (distances[0][k], 0)

    for subset_size in range(2, n):
        for subset in itertools.combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev_bits = bits & ~(1 << k)
                res = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    res.append((C[(prev_bits, m)][0] + distances[m][k], m))
                C[(bits, k)] = min(res)

    bits = (2**n - 1) - 1
    res = []
    routes = []
    for k in range(1, n):
        res.append((C[(bits, k)][0] + distances[k][0], k))
        routes.append(C[(bits, k)][1])
    opt, parent = min(res)

    return routes, opt
