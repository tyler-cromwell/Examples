"""
Returns a Longest Common Subsequence between the given strings.
"""
def longest_common_subsequence(s1, s2):
    table = []
    result = []
    n = len(s1)
    m = len(s2)
    i = 0
    j = 0

    """
    Initialize table.
    """
    for r in range(n+1):
        table.append([0] * (m+1))

    """
    Compute table.
    """
    for r in range(1, n+1):
        for c in range(1, m+1):
            if s1[i] == s2[j]:
                table[r][c] = table[r-1][c-1] + 1
            elif table[r-1][c] >= table[r][c-1]:
                table[r][c] = table[r-1][c]
            else:
                table[r][c] = table[r][c-1]
            j += 1
        j = 0
        i += 1

    """
    Construct result.
    """
    for r in range(n, 0, -1):
        for c in range(m, 0, -1):
            if table[r][c] > table[r-1][c] and table[r][c] > table[r][c-1]:
                result.append(s1[r-1])
                m -= 1
                break
            elif table[r][c] == table[r-1][c] and table[r][c] > table[r][c-1]:
                break
            else:
                m -= 1
                continue

    return ''.join(reversed(result))


"""
Returns a Longest Common Substring between the given strings.
"""
def longest_common_substring(s1, s2):
    table = []
    n = len(s1)
    m = len(s2)
    i = 0
    j = 0
    value = 0
    cell = (1, 1)

    """
    Initialize table.
    """
    for r in range(n+1):
        table.append([0] * (m+1))

    """
    Compute table.
    """
    for r in range(1, n+1):
        for c in range(1, m+1):
           if s1[i] == s2[j]:
               table[r][c] = table[r-1][c-1] + 1
               if table[r][c] > value:
                   cell = (r, c)
                   value = table[r][c]
           j += 1
        j = 0
        i += 1

    """
    Traceback.
    """
    i = cell[0]
    j = cell[1]
    l = table[i][j]
    result = [''] * l

    for a in range(l-1, -1, -1):
        result[a] = s1[i-1]
        i -= 1
        j -= 1

    return ''.join(result)


"""
Function aliases.
"""
lcsq = longest_common_subsequence
lcst = longest_common_substring
