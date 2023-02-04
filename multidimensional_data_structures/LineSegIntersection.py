import csv


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def on_segment(p, q, r):
    if max(p.x, r.x) >= q.x >= min(p.x, r.x) and max(p.y, r.y) >= q.y >= min(p.y, r.y):
        return True
    return False


def cross_product(p1, p2, p3):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def orientation(p, q, r):
    val = cross_product(p, q, r)
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise


def do_intersect(p1, q1, p2, q2):
    r = Point(q2.x - p1.x, q2.y - p1.y)
    s = Point(q1.x - p2.x, q1.y - p2.y)
    val = cross_product(p1, q2, q1)
    if val == 0:
        return False
    t = cross_product(p2, q2, q1) / val
    if t < 0 or t > 1:
        return False
    u = cross_product(p1, q2, p2) / val
    if u < 0 or u > 1:
        return False
    return True


def line_segment_intersection(x):
    n = len(x)
    for i in range(n):
        for j in range(i + 1, n):
            p1 = x[i]
            q1 = x[j]
            p2 = x[(i + 1) % n]
            q2 = x[(j + 1) % n]
            if do_intersect(p1, q1, p2, q2):
                return True
    return False


# Open the CSV file and add the points in the arrays
points = []
with open('coordinates.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)

    # p and q are the two points of a line

    # Insert the coordinates of each line
    for row in reader:
        p = Point(float(row[0]), float(row[1]))
        q = Point(float(row[2]), float(row[3]))
        points.append(p)
        points.append(q)

for i in range(0, len(points) - 1, 2):
    for j in range(0, len(points) - 1, 2):
        if do_intersect(points[i], points[i + 1], points[j], points[j + 1]):
            print("Lines {},{}-{},{} and {},{}-{},{} intersect".format(int(points[i].x), int(points[i].y),
                                                                       int(points[i + 1].x), int(points[i + 1].y),
                                                                       int(points[j].x), int(points[j].y),
                                                                       int(points[j + 1].x), int(points[j + 1].y)))
