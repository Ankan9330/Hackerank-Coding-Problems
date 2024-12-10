'''The distance between two array values is the number of indices between them. Given , find the minimum distance between any pair of equal elements in the array. If no such value exists, return .

Example

There are two matching pairs of values:  and . The indices of the 's are  and , so their distance is . The indices of the 's are  and , so their distance is . The minimum distance is .

Function Description

Complete the minimumDistances function in the editor below.

minimumDistances has the following parameter(s):

int a[n]: an array of integers
Returns

int: the minimum distance found or  if there are no matching elements
Input Format

The first line contains an integer , the size of array .
The second line contains  space-separated integers .

Constraints

Output Format

Print a single integer denoting the minimum  in . If no such value exists, print .

Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
7 1 3 4 1 7     arr = [7, 1, 3, 4, 1, 7]
Sample Output

3
Explanation
There are two pairs to consider:

 and  are both , so .
 and  are both , so .
The answer is .'''
def beautifulTriplets(d, arr):
    n = len(arr)
    
    left_count = [0] * n
    right_count = [0] * n
    beautiful_triplet_count = 0

    # Counting valid pairs for left_count using a hashmap
    left_map = {}
    for j in range(1, n):
        count = left_map.get(arr[j] - d, 0)
        left_count[j] = count
        if arr[j] in left_map:
            left_map[arr[j]] += 1
        else:
            left_map[arr[j]] = 1

    # Counting valid pairs for right_count using a hashmap
    right_map = {}
    for j in range(n - 2, -1, -1):
        count = right_map.get(arr[j] + d, 0)
        right_count[j] = count
        if arr[j] in right_map:
            right_map[arr[j]] += 1
        else:
            right_map[arr[j]] = 1

    # Counting total beautiful triplets
    for j in range(1, n - 1):
        beautiful_triplet_count += left_count[j] * right_count[j]

    return beautiful_triplet_count
