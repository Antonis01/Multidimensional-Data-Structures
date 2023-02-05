import LineSegIntersection


def main():
    points = [(1, 3), (2, 4), (3, 5), (4, 7), (6, 8), (8, 9), (9, 10)]
    from Intervaltree import IntervalTree
    from Intervaltree import Interval

    it = IntervalTree()
    for point in points:
        it.insert(Interval(*point))

    from Segment import SegmentTree
    st = SegmentTree(points)

    while True:
        print("\nSelect an option:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Option 1 code here
            print("You selected Option 1")
        elif choice == 2:
            # Option 2 code here
            print("You selected Option 2")
            print("--------------------")
            print("You selected interval/segment tree:")
            print("1. Interval Tree Interval Query")
            print("2. SegmentTree Stabbing Query")
            print("3 exit")
            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                print("Enter interval to search (start end):")
                start, end = map(int, input().split())
                it.search(Interval(start, end))
            elif choice2 == 2:
                print("You selected Insert SegmentTree")
                print("Enter the segment:")
                x = int(input("Enter x coordinate for Stabbing Query: "))
                result = st.query(0, 0, st.n - 1, 0, x)
                print("Max y value for x <=", x, "is:", result)
            elif choice2 == 3:
                print("You selected Option 2.3")
                print("Exiting program...")
                break
            else:
                print("Invalid choice")

        elif choice == 3:
            # Option 3 code here
            print("Convex Hull")
            from ConvexHull import ConvexHull
            hull = ConvexHull(points)
            result = hull.find_hull()
            print("Convex Hull:", result)
        elif choice == 4:
            print("You selected Option 4")
            LineSegIntersection.run_lineSegInter()
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()
