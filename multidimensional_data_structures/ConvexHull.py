class ConvexHull:
    def __init__(self, points):
        self.points = points
        self.hull = []

    def find_hull(self):
        points = self.points

        # Find the leftmost point
        start = points[0]
        for p in points[1:]:
            if p[0] < start[0]:
                start = p

        # Initialize the current point to the leftmost point
        current = start
        while True:
            self.hull.append(current)

            # Search for the next point to add to the hull
            next_point = points[0]
            for p in points[1:]:
                # Check if p is on the right of the line from current to next_point
                if (next_point[0] - current[0]) * (p[1] - current[1]) - (next_point[1] - current[1]) * (
                        p[0] - current[0]) > 0:
                    next_point = p

            # If the next point is the starting point, we have found the hull
            current = next_point
            if current == start:
                break

        return self.hull
