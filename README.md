# Closest Pair Problem Daa Assignment

### Name - Samiksha Anasane
### Roll no- 18

## Problem Statement: 
Implement a solution to find a minimum distance between two points.
Input array: each element defined as [a,b] for example [2,3]
Use distance formula.

## Theory: In this problem we have given a set of points on a 2D plane, and we have to find the pair of points, whose distance is minimum.

## Approach:

1. Sort the points on the basis of X co-ordinate, and find the mid point.
2. Find the closest pair on the left and right of mid points(say min1 and min2) and their distances, Recursively.
3. Find the minimum between min1 and min2 (say minD)
4. There are two cases on the basis of where the closest pair may exit:
	1.If a closest pair exist other than min1 and min2 it will lie on a band that spans for minD distance from the midpoint
	2.if one of them is outside the band then distance between them will always be greater than minD. 
So, We need to traverse the points that are inside the band only. 
5. Sort the points in the band according to the Y co-ordinate.
6. Traverse all the points, for every point if a point with distance minD exists it will be within the minD x minD rectangle 
   which will contain atmost 6 points.
7. Then traverse the 6 next points for each point in the inside band array return the closest pair.


## Complexity:

The complexity of the algorithm is O(nlogn)

Explaination: 

  1.Sorting of X and Y values => O(nlogn)
  2.Splitting of X sorted and Y sorted values => n 
  3.Recursive call for the left part for the right part =>T(n/2)+T(n/2)
  4.Finding the points that are in the band => n
  5.For checking the six points in the band for every point => 6n

## Test Cases:
```
### Test case 1: points array = (5, 1), (19, 25), (50, 25), (3, 4), (2, 1), (30, 14)
Closest pair:
Point1: (2, 1) 
Point2: (5, 1)
Distance between point1 and point2: 3.0

### Test case 2: points array = (20, 4), (9, 8), (5, 10), (4, 4), (2, 0), (18, 21)
Closest pair:
Point1: (-1, 0) 
Point2: (0, 5)
Distance between point1 and point2: 4.47213595499958


### Test case 3: points array = (-100, 10), (99, 20), (0, 55), (300, 44), (170, 2), (3, 140)
Closest pair:
Point1: (99, 20), 
Point2: (170, 2)
Distance between point1 and point2: 73.24616030891995

```
