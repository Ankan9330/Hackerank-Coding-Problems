'''Given a set of distinct integers, print the size of a maximal subset of  where the sum of any  numbers in  is not evenly divisible by .

Example
 

One of the arrays that can be created is . Another is . After testing all permutations, the maximum length solution array has  elements.

Function Description

Complete the nonDivisibleSubset function in the editor below.

nonDivisibleSubset has the following parameter(s):

int S[n]: an array of integers
int k: the divisor
Returns

int: the length of the longest subset of  meeting the criteria
Input Format

The first line contains  space-separated integers,  and , the number of values in  and the non factor.
The second line contains  space-separated integers, each an , the unique values of the set.

Constraints

All of the given numbers are distinct.
Sample Input

STDIN    Function
-----    --------
4 3      S[] size n = 4, k = 3
1 7 2 4  S = [1, 7, 2, 4]
Sample Output

3
Explanation

The sums of all permutations of two elements from  are:

1 + 7 = 8
1 + 2 = 3
1 + 4 = 5
7 + 2 = 9
7 + 4 = 11
2 + 4 = 6
Only  will not ever sum to a multiple of .'''
import os
import collections


def nonDivisibleSubset(k, s):
    dic = collections.Counter()

    for i in s:
        dic[i % k] += 1

    answer = min(dic[0], 1)

    for r in range(1,k//2+1):
        if r != k/2:
            answer += max(dic[r], dic[k-r])

    if k % 2 == 0:
        answer += 1

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result))
    fptr.close()