import LineSegInter3D
import LineSegIntersection
import timeit
import rtree3d


def main():
    points = [(1, 3), (2, 4), (3, 5), (4, 7), (6, 8), (8, 9), (9, 10)]
    from Intervaltree import IntervalTree
    from Intervaltree import Interval

    starttimer1 = timeit.default_timer()
    it = IntervalTree()
    for point in points:
        it.insert(Interval(*point))
    endtimer1 = timeit.default_timer()
    timetaken1 = endtimer1 - starttimer1

    starttimer2 = timeit.default_timer()
    from Segment import SegmentTree
    st = SegmentTree(points)
    endtimer2 = timeit.default_timer()
    timetaken2 = endtimer2 - starttimer2

    while True:
        print("\nSelect an option:")
        print("1. Exercise 1")
        print("2. Exercise 2")
        print("3. Exercise 3")
        print("4. Exercise 4")
        print("5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            # Option 1 code here
            print("You selected Option 1")
            rtree3d.run_3drtree()

        elif choice == 2:
            # Option 2 code here
            print("\nYou selected Option 2")
            print("--------------------")
            print("You selected interval/segment tree:")
            print("1. Interval Tree Interval Query")
            print("2. SegmentTree Stabbing Query")
            print("3. Compare time for both")
            print("4. exit")
            choice2 = int(input("Enter your choice: "))
            if choice2 == 1:
                print("Enter interval to search (start end):")
                start, end = map(int, input().split())
                it.search(Interval(start, end))

            elif choice2 == 2:
                print("You selected Insert SegmentTree")
                print("Enter the segment:")
                x = input("Enter x coordinate for Stabbing Query: ")
                try:
                    x = int(x)
                    res = st.query(0, 0, st.n - 1, x)
                    if res == 0:
                        print("No points found")
                    else:
                        print("Maximum y:", res)
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            elif choice2 == 3:
                print ("You selected: Compare time for both")
                print("time for interval tree:", timetaken1)
                print("time for segment tree:", timetaken2)
                if timetaken1 > timetaken2:
                    print("Segment tree is faster")
                else:
                    print("Interval tree is faster")
            elif choice2 == 4:
                print("Exiting program...")
                break
            else:
                print("Invalid choice")

        elif choice == 3:
            print("Convex Hull\n")
            from ConvexHull import ConvexHull
            hull = ConvexHull(points)
            result = hull.find_hull()
            print("Convex Hull:", result)
        elif choice == 4:
            print("Line segment Intersection\n1) 2D\n2) 3D\n")
            choice3 = int(input("Enter your choice: "))
            if choice3 == 1:
                LineSegIntersection.run_lineSegInter()
            elif choice3 == 2:
                LineSegInter3D.run_lineSegInter3D()
            else:
                print("Wrong Input")
        elif choice == 5:
            print("Exiting program...")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()
