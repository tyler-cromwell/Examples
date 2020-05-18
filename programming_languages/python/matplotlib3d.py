from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)


if __name__ == '__main__':
    points = [
        Point(0, 0, 0),
        Point(1, 0, 0),
        Point(0, 1, 0),
        Point(0, 0, 1),
        Point(1, 1, 0),
        Point(1, 0, 1),
        Point(0, 1, 1),
        Point(1, 1, 1)
    ]

    xs = [point.x for point in points]
    ys = [point.y for point in points]
    zs = [point.z for point in points]

    fig = plt.figure()
    fig.suptitle('image'.capitalize(), fontsize=20)
    ax = fig.add_subplot(111, projection='3d')

    for i, point in enumerate(points):
        ax.text(point.x, point.y, point.z, point)

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xlabel('X', fontsize=12)
    ax.set_ylabel('Y', fontsize=12)
    ax.set_zlabel('Z', fontsize=12)
    ax.scatter(xs=xs, ys=ys, zs=zs)
    plt.savefig('image.png')        
