#! /usr/bin/env python3
from math import sqrt

def L1(a,b):
    return (abs(a[0] - b[0]) + abs(a[1] - b[1]))

def L2(a,b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

points = [2, 10 , 2, 5, 8,4, 5,8,7,5,6,4,1,2,4,9]
distance_function = L2

x = [points[i] for i in range(0,len(points),2)]
y = [points[i] for i in range(1,len(points),2)]
data_points = [[x1,y1] for x1 , y1 in zip(x,y)]
print("Data Points " , data_points)

def printTable(centers, t):
    print("\n ", t, end="\t\t")
    for center in centers:
        print("[{0:.2f}".format(center[0]), ",{0:.2f}]".format(center[1]) ,end = "\t")
    print("\n-----------------------------------------------------------")


    for data_point in data_points:
        min_dist = float('inf')
        min_center = [0,0]

        print(data_point, end = "\t\t")
        for center in centers:
            print("{0:.2f}".format(L2(center ,data_point)), end = "\t\t")
            if(L2(center ,data_point) < min_dist):
                min_dist = L2(center ,data_point)
                min_center = center

        print("\t", "[{0:.2f}".format(min_center[0]), ",{0:.2f}]".format(min_center[1]))   

#Marking the centers for each point, initially marked as 0
center_points = [[0,0] for i in range(0,len(data_points))]

# choose the k initial seeds

k = 3
center_index = [0,3,6]
centers = [data_points[center_index[i] ] for i in range(0,len(center_index))]

t = 1
error = float('inf')

while(error > 0.0001):
    printTable(centers, t)

    t += 1
    for i in range(len(data_points)):
        distancesMin = float('inf')

        # compute the distance and assign pts to respt clusters
        for c in centers:
            currDistance = distance_function(c, data_points[i])
            if(currDistance < distancesMin):
                distancesMin = currDistance
                center_points[i] = c


    new_centers = [[0,0] for i in range(len(centers))]
    no_of_points = [0 for i in range(len(centers))]

    for i in range(len(center_points)):
        for c in range(len(centers)):
            if center_points[i] == centers[c]:
                new_centers[c][0] += data_points[i][0]
                new_centers[c][1] += data_points[i][1]
                no_of_points[c] += 1

    error = 0
    for c in range(len(centers)):
        new_centers[c][0] /= no_of_points[c]
        new_centers[c][1] /= no_of_points[c]
        error += distance_function(new_centers[c], centers[c])

    centers = new_centers
    

          



# calculate the centroid and assign them as the new centers
# Repeat until the centroid positions do not change