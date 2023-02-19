import numpy as np
import matplotlib.pyplot as plt
import random


def line_seg_intersect(a, b, c, d):
    r = b - a
    s = d - c
    q = d - c

    qr = np.dot(q, r)
    qs = np.dot(q, s)
    rs = np.dot(r, s)
    rr = np.dot(r, r)
    ss = np.dot(s, s)

    denom = rr * ss - rs * rs
    if denom == 0:
        return False

    t = qs * rs - qr * ss / denom
    u = (qs + t * rs) / ss

    p0 = a + t * r
    p1 = c + u * s

    on_segment = False
    intersects = False

    if 0 <= t <= 1 and 0 <= u <= 1:
        on_segment = True
    if np.linalg.norm(p0-p1) == 0:
        intersects = True
    if on_segment is True and intersects is True:
        return True


def generate_random_line():
    # Generate two random points in 3D space to define a line segment
    point1 = np.array([random.randint(0, 5) for i in range(3)])
    point2 = np.array([random.randint(0, 5) for i in range(3)])
    return point1, point2


def plot_lines(p1, p2, p3, p4):
    # Plot the line segments in 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # [x-coordinates of the line], [y-coordinates of the line], [z-coordinates of the line]
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], 'r')
    ax.plot([p3[0], p4[0]], [p3[1], p4[1]], [p3[2], p4[2]], 'b')
    ax.set_title("Intersects")
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()


def run_lineSegInter3D():
    while True:
        # Generate two random line segments
        x1, y1 = generate_random_line()
        x2, y2 = generate_random_line()

        if line_seg_intersect(x1, y1, x2, y2):
            print(
                "Lines {},{},{}-{},{},{} and {},{},{}-{},{},{} do intersect".format(int(x1[0]), int(x1[1]), int(x1[2]),
                                                                                    int(y1[0]), int(y1[1]), int(y1[2]),
                                                                                    int(x2[0]), int(x2[1]), int(x2[2]),
                                                                                    int(y2[0]), int(y2[1]), int(y2[2])))
            plot_lines(x1, y1, x2, y2)
            break
