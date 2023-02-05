from rtree import index
import csv
import math
import matplotlib.pyplot as plt

# Create a 3D R-tree index
p = index.Property()
p.dimension = 3
idx = index.Index(properties=p)

# open the csv file
with open("ex1_object_coordinates.csv") as csvfile:
    data = csv.DictReader(csvfile)
    counter = 0
    for row in data:
        # insert data into the tree
        id = row['id']
        x = row['x']
        y = row['y']
        t = row['time']
        idx.insert(int(id), (int(x), int(y), int(t), float(x), float(y), int(t)))


def print_tree_contents(rtree_index):
    for item in rtree_index.intersection((-math.inf, -math.inf, -math.inf, math.inf, math.inf, math.inf), objects=True):
        x, y, t = item.bbox[0],item.bbox[1],item.bbox[2]
        print("ID:", item.id, " X:", x, " Y:", y, " T:", t)


# Query for all points within a certain time range
def query_time_range(rtree_index, start_seconds, end_seconds):
    # use the intersection method to find all the points within the time range
    results = rtree_index.intersection((-math.inf, -math.inf, start_seconds, math.inf, math.inf, end_seconds), objects=True)
    # iterate over the results and print the id, x, y, and t values
    for item in results:
        x, y, t = item.bbox[0], item.bbox[1], item.bbox[2]
        print("ID:", item.id, " X:", x, " Y:", y, " T:", t)


# Query for all points within a certain spatial area
def query_bounding_box(rtree_index, min_x, min_y, max_x, max_y):
    # use the intersection method to find all the points within the bounding box
    results = rtree_index.intersection((min_x, min_y, -math.inf, max_x, max_y, math.inf), objects=True)
    # iterate over the results and print the id, x, y, and t values
    for item in results:
        x, y, t = item.bbox[0],item.bbox[1],item.bbox[2]
        print("ID:", item.id, " X:", x, " Y:", y, " T:", t)


# Query for all the points that are in a specific area and time range
def query_area_and_time_range(rtree_index, min_x, min_y, max_x, max_y, start_seconds, end_seconds):
    # use the intersection method to find all the points within the area and time range
    results = rtree_index.intersection((min_x, min_y, start_seconds, max_x, max_y, end_seconds), objects=True)
    # iterate over the results and print the id, x, y, and t values
    for item in results:
        x, y, t = item.bbox[0], item.bbox[1], item.bbox[2]
        print("ID:", item.id, " X:", x, " Y:", y, " T:",t )


def visualize_data_3d(rtree_index):
    # extract x,y,t values from the tree
    x = []
    y = []
    t = []
    for item in rtree_index.intersection((-math.inf, -math.inf, -math.inf, math.inf, math.inf, math.inf), objects=True):
        x.append(int(item.bbox[0]))
        y.append(int(item.bbox[1]))
        t.append(int(item.bbox[2]))

    # create the 3D scatter plot
    ax = plt.axes(projection="3d")
    ax.plot(t, x, y)
    ax.set_xlabel('Time')
    ax.set_ylabel('x')
    ax.set_zlabel('y')
    ax.view_init(elev=20, azim=0)
    plt.show()


visualize_data_3d(idx)


def run_3drtree():
    print()
    print("-----3D R-tree for Spatio-Temporal Queries-----")
    print()
    print("Queries Available: ")
    print("1. Query for all points within a certain time range")
    print("2. Query for all points within a certain spatial area")
    print("3. Query for all the points that are in a specific area and time range")
    print("-----------------------------------------------")
    print("4. Show R-tree Data")
    print()
    option = int(input("Select an Option: "))

    if option == 1:
        print("Selected Query for all points within a certain time range")
        print("Please Enter Time Range")
        start = int(input("From:"))
        end = int(input("To:"))
        query_time_range(idx, start, end)
        print("Showing All Points Within", start, "῀", end, " Seconds")
    elif option == 2:
        print("Selected Query for all points within a certain spatial area")
        print("Enter Minimum Point Coordinates")
        minimum_x = float(input("x:"))
        minimum_y = float(input("y:"))
        print("Enter Maximum Point Coordinates")
        maximum_x = float(input("x:"))
        maximum_y = float(input("y:"))
        query_bounding_box(idx, minimum_x, minimum_y, maximum_x, maximum_y)
        print("Showing All Points Within Spatial Area: ", "(", minimum_x, ",", minimum_y, ")", "῀(", maximum_x, ",",
              maximum_y, ")")
    elif option == 3:
        print("Selected Query for all the points that are in a specific area and time range")
        print("Enter Minimum Point Coordinates")
        minimum_x = float(input("x:"))
        minimum_y = float(input("y:"))
        print("Enter Maximum Point Coordinates")
        maximum_x = float(input("x:"))
        maximum_y = float(input("y:"))
        print("Please Enter Time Range")
        start = int(input("From:"))
        end = int(input("To:"))
        query_area_and_time_range(idx, minimum_x, minimum_y, maximum_x, maximum_y, start, end)
        print("Showing All Points Within Spatial Area: ", "(", minimum_x, ",", minimum_y, ")", "῀(", maximum_x, ",",
              maximum_y, ")")
        print("AND")
        print("Within", start, "῀", end, " Seconds")
    elif option == 4:
        print("Printing Data..")
        print_tree_contents(idx)
    else:
        print("Wrong Input")
