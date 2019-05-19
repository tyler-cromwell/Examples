#!/usr/bin/env python3

# http://cgm.cs.mcgill.ca/~athens/cs601/
# http://www.ams.sunysb.edu/~jsbm/courses/345/13/melkman.pdf
# http://geomalgorithms.com/a12-_hull-3.html


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return '({},{})'.format(self._x, self._y)
 
    def x(self):
        return self._x

    def y(self):
        return self._y


def print_hull(H):
    for p in hull:
        print(p)
    print()


def ccw(p1, p2, p3):
    value = (p1.x() * ((p2.y() * 1) - (p3.y() * 1))) \
          - (p2.x() * ((p1.y() * 1) - (p3.y() * 1))) \
          + (p3.x() * ((p1.y() * 1) - (p2.y() * 1)))

    if value > 0: return 1
    elif value < 0: return -1
    else: return 0


"""
Computes the Convex Hull of a simple polygon.

P is a polyine outlining the simple polygon.
"""
def melkman(P):
    n = len(P)
    H = []
    D = [0] * n

    bot = 0
    top = bot+3
    D[bot] = D[top] = P[2]

    if ccw(P[0], P[1], P[2]) > 0:
        D[bot+1] = P[0]
        D[bot+2] = P[1]
    else:
        D[bot+1] = P[1]
        D[bot+2] = P[0]

    for i in range(3, n):
        next_point = P[i]
        print('####################')
        print('Step', i-2)
        print('Deque:', next_point, [str(a) for a in D])
        if ccw(D[bot], D[bot+1], next_point) > 0 and ccw(D[top-1], D[top], next_point) > 0:
            continue

        while ccw(D[bot], D[bot+1], next_point) <= 0:
            bot += 1
        bot -= 1
        D[bot] = next_point

        while ccw(D[top-1], D[top], next_point) <= 0:
            top -= 1
        top += 1
        D[top] = next_point

        H_fake = []
        for h in range(1, top-bot+1):
            H_fake.append(D[bot+h])
        print('TENTATIVE:', [str(a) for a in H_fake])

    print('####################')
    for h in range(1, top-bot+1):
        H.append(D[bot+h])

    return H


if __name__ == '__main__':
    polyline = [
        Point(2,2),     # hull
        Point(5,3),
        Point(8,2),     # hull
        Point(10,9),    # hull
        Point(5,7),
        Point(3,7)      # hull
    ]
    hull = melkman(polyline)
    print('Convex Hull:')
    print_hull(hull)

    polyline = [
        Point(2,2),     # hull
        Point(5,3),
        Point(8,2),     # hull
        Point(7,5),
        Point(10,9),    # hull
        Point(5,7),
        Point(3,7)      # hull
    ]
    hull = melkman(polyline)
    print('Hull:')
    print_hull(hull)
