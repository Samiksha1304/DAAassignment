import math


def distance(p1, p2):
    return math.dist(p1, p2)


def brute_force(points):
    minimum_dist = float("inf")
    p1 = None
    p2 = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = distance(points[i], points[j])
            if d < minimum_dist:
                minimum_dist = d
                p1 = points[i]
                p2 = points[j]
    return p1, p2, minimum_dist


def recursion(xsort, ysort):
    n = len(xsort)
    if n <= 3:
        return brute_force(xsort)
    else:
        ysorted_l = []
        ysorted_r = []
        mid = xsort[n//2]
        xsorted_l = xsort[:n//2]
        xsorted_r = xsort[n//2:]

        for point in ysort:
            ysorted_l.append(point) if (
                point[0] <= mid[0]) else ysorted_r.append(point)

        (p1_l, p2_l, dl) = recursion(xsorted_l, ysorted_l)
        (p1_r, p2_r, dr) = recursion(xsorted_r, ysorted_r)

        (p1, p2, x) = (p1_l, p2_l, dl) if (dl < dr) else (p1_r, p2_r, dr)

        in_band = [point for point in ysort if mid[0] -
                   x < point[0] < mid[0]+x]

        for i in range(len(in_band)):
            for j in range(i+1, min(i+7, len(in_band))):
                d = distance(in_band[i], in_band[j])
                if d < x:
                    print(in_band[i], in_band[j])
                    (p1, p2, x) = (in_band[i], in_band[j], d)
        return p1, p2, x


def closest_pair(points):
    xsort = sorted(points, key=lambda point: point[0])
    ysort = sorted(points, key=lambda point: point[1])
    return recursion(xsort, ysort)


points = [(-100, 10), (99, 20), (0, 55), (300, 44), (170, 2), (3, 140)]

print("\nResult:")
print("The shortest distance between the points is: ", closest_pair(points))
print("\n\n")
