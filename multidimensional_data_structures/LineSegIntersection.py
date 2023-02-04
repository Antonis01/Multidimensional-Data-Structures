import csv
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# The function checks if point q1 lies online segment p1,r
# based on the 3 collinear points
def on_segment(p1, q1, r):
    if max(p1.x, r.x) >= q1.x >= min(p1.x, r.x) and max(p1.y, r.y) >= q1.y >= min(p1.y, r.y):
        return True
    return False


# finding the orientation of the 3 points
def orientation(a, b, r):
    val = (b.y - a.y) * (r.x - b.x) - (b.x - a.x) * (r.y - b.y)
    if val == 0:
        # collinear
        return 0
    elif val > 0:
        # clockwise
        return 1
    else:
        # counterclockwise
        return 2


def do_intersect(p1, q1, p2, q2):
    # We find the orientation using the p and q of each point
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if o1 != o2 and o3 != o4:
        return True

    # p1,q1,p2 are collinear
    # p2 lies on segment p1,q1
    if o1 == 0 and on_segment(p1, p2, q1):
        return True

    # p1,q1,q2 are collinear
    # q2 lies on segment p1,q1
    if o2 == 0 and on_segment(p1, q2, q1):
        return True

    # p2,q2,p1 are collinear
    # p1 lies on segment p2,q2
    if o3 == 0 and on_segment(p2, q1, q2):
        return True

    # p2,q2,q1 are collinear
    # p1 lies on segment p2,q2
    if o4 == 0 and on_segment(p2, q1, q2):
        return True

    return False


# Open the CSV file and add the points in the arrays
points = []
with open('coordinates.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)

    # p and q are the two points of a line
    # Insert the coordinates of each line
    for row in reader:
        # Adds the columns to x and y of p and q
        # So now we have p.x,p.y and q.x,q.y
        p = Point(float(row[0]), float(row[1]))
        q = Point(float(row[2]), float(row[3]))
        # Add those two points in an array
        points.append(p)
        points.append(q)


for i in range(0, len(points) - 1, 2):
    # we start from i + 2 in the second for loop because we don't want to check two times for every point
    # because the array is 1D
    for j in range(i + 2, len(points) - 1, 2):
        if do_intersect(points[i], points[i + 1], points[j], points[j + 1]):
            print("Lines {},{}-{},{} and {},{}-{},{} intersect".format(int(points[i].x), int(points[i].y),
                                                                       int(points[i + 1].x), int(points[i + 1].y),
                                                                       int(points[j].x), int(points[j].y),
                                                                       int(points[j + 1].x), int(points[j + 1].y)))

            # we make and show the plot for the lines that intersect 
            plt.figure(figsize=(5, 5))
            plt.plot((int(points[i].x), int(points[i + 1].x)), (int(points[i].y), int(points[i + 1].y)), '.r--')
            plt.plot((int(points[j].x), int(points[j + 1].x)), (int(points[j].y), int(points[j + 1].y)), '.b--')
            plt.show()
