'''Given a sequence of integers , a triplet  is beautiful if:

Given an increasing sequenc of integers and the value of , count the number of beautiful triplets in the sequence.

Example


There are three beautiful triplets, by index: . To test the first triplet,  and .

Function Description

Complete the beautifulTriplets function in the editor below.

beautifulTriplets has the following parameters:

int d: the value to match
int arr[n]: the sequence, sorted ascending
Returns

int: the number of beautiful triplets
Input Format

The first line contains  space-separated integers,  and , the length of the sequence and the beautiful difference.
The second line contains  space-separated integers .

Constraints

Sample Input

STDIN           Function
-----           --------
7 3             arr[] size n = 7, d = 3
1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]
Sample Output

3
Explanation

There are many possible triplets , but our only beautiful triplets are  ,  and  by value, not index. Please see the equations below:




Recall that a beautiful triplet satisfies the following equivalence relation:  where .'''
def minimumdistance(a):
    last_seen = {}
    min_distance=float('inf')
    for i,value in enumerate(a):
        if value in last_seen:
            distance = i - last_seen[value]
            min_distance=min(distance,min_distance)
        last_seen[value] = i
    return min_distance if min_distance != float('inf') else -1
