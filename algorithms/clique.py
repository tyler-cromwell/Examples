import itertools


N = [
    [1, 2, 3, 5, 7],
    [0, 2, 4, 6],
    [0, 1, 3, 4],
    [0, 2, 4, 5, 6, 7],
    [1, 2, 3, 5, 6, 8],
    [0, 3, 4, 6, 7],
    [1, 3, 4, 5, 8],
    [0, 3, 5],
    [4, 6]
]
V = []
E = []


def find_clique(k):
    count = 0
    clique = []

    for group in list(itertools.combinations(V, k)):
        edges = list(itertools.combinations(group, 2))
        n = len(edges)

        for edge in edges:
            if edge in E:
                count += 1

        if count == n:
            clique.append(group)
            return True, clique
        else:
            count = 0
            clique = []

    return False, clique


if __name__ == '__main__':
    for v in range(len(N)):
        V.append(v)

    for v in range(len(N)):
        for n in N[v]:
            E.append((v, n))

    print(find_clique(k=4))
