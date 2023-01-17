from rtree import index
import csv
from datetime import datetime
import math
import matplotlib.pyplot as plt

# Create a 3D R-tree index
p = index.Property()
p.dimension = 3
idx = index.Index(properties=p)

# open the csv file
with open("ask1data.csv") as csvfile:
    data = csv.DictReader(csvfile)
    counter = 0
    for row in data:
        # insert data into the tree
        id = row['id']
        x = row['lat']
        y = row['lon']
        t = row['time']
        str(t)
        x = (float(x)- 33.80)*100000
        y = (float(y) - 112.13)*1000000
        time = datetime.strptime(t, "%H:%M:%S")
        total_seconds = (time - datetime(1900, 1, 1)).total_seconds() - 73968.0

        idx.insert(int(id), (int(x),int(y),float(total_seconds), float(x),float(y),float(total_seconds)))

def print_tree_contents(rtree_index):
    for item in rtree_index.intersection((-math.inf, -math.inf, -math.inf, math.inf, math.inf, math.inf), objects=True):
        x, y, t = item.bbox[0],item.bbox[1],item.bbox[2]
        print("ID:",item.id," X:",x," Y:",y," T:",t)

#Query for all points within a certain time range
def query_time_range(rtree_index, start_seconds, end_seconds):
    #use the intersection method to find all the points within the time range
    results = rtree_index.intersection((-math.inf, -math.inf, start_seconds, math.inf, math.inf, end_seconds), objects=True)
    #iterate over the results and print the id, x, y, and t values
    for item in results:
        x, y, t = item.bbox[0],item.bbox[1],item.bbox[2]
        print("ID:",item.id," X:",x," Y:",y," T:",t)

#Query for all points within a certain spatial area
def query_bounding_box(rtree_index, min_x, min_y, max_x, max_y):
    #use the intersection method to find all the points within the bounding box
    results = rtree_index.intersection((min_x, min_y, -math.inf, max_x, max_y, math.inf), objects=True)
    #iterate over the results and print the id, x, y, and t values
    for item in results:
        x, y, t = item.bbox[0],item.bbox[1],item.bbox[2]
        print("ID:",item.id," X:",x," Y:",y," T:",t)

#Query for all the points that are in a specific area and time range
def query_area_and_time_range(rtree_index, min_x, min_y, max_x, max_y, start_seconds, end_seconds):
    #use the intersection method to find all the points within the area and time range
    results = rtree_index.intersection((min_x, min_y, start_seconds, max_x, max_y, end_seconds), objects=True)
    #iterate over the results and print the id, x, y, and t values
    for item in results:
        x, y, t = item.bbox[0],item.bbox[1],item.bbox[2]
        print("ID:",item.id," X:",x," Y:",y," T:",t)

def visualize_data_3d(rtree_index):
    # extract x,y,t values from the tree
    x = []
    y = []
    t = []
    for item in rtree_index.intersection((-math.inf, -math.inf, -math.inf, math.inf, math.inf, math.inf), objects=True):
        x.append(item.bbox[0])
        y.append(item.bbox[1])
        t.append(item.bbox[2])

    # create the 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, t)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_zlabel('Time')
    #ax.view_init(elev=20, azim=350)
    plt.show()

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
    query_time_range(idx,start,end)
    print("Showing All Points Within", start, "῀", end, " Seconds")
elif option == 2:
    print("Selected Query for all points within a certain spatial area")
    print("Enter Minimum Point Coordinates")
    minimum_x = float(input("x:"))
    minimum_y = float(input("y:"))
    print("Enter Maximum Point Coordinates")
    maximum_x = float(input("x:"))
    maximum_y = float(input("y:"))
    query_bounding_box(idx,minimum_x,minimum_y,maximum_x,maximum_y)
    print("Showing All Points Within Spatial Area: ", "(",minimum_x,",",minimum_y,")","῀(",maximum_x,",",maximum_y,")")
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
    query_area_and_time_range(idx,minimum_x,minimum_y,maximum_x,maximum_y,start,end)
    print("Showing All Points Within Spatial Area: ", "(", minimum_x, ",", minimum_y, ")", "῀(", maximum_x, ",",maximum_y, ")")
    print("AND")
    print("Within", start, "῀", end, " Seconds")
elif option == 4:
    print("Printing Data..")
    print_tree_contents(idx)
else:
    print("Wrong Input")