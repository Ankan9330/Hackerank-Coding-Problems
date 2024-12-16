'''There is a strange counter. At the first second, it displays the number . Each second, the number displayed by decrements by  until it reaches . In next second, the timer resets to  and continues counting down. The diagram below shows the counter values for each time  in the first three cycles:

strange(1).png

Find and print the value displayed by the counter at time .

Function Description

Complete the strangeCounter function in the editor below.

strangeCounter has the following parameter(s):

int t: an integer
Returns

int: the value displayed at time 
Input Format

A single integer, the value of .

Constraints

Subtask

 for  of the maximum score.
Sample Input

4
Sample Output

6
Explanation

Time  marks the beginning of the second cycle. It is double the number displayed at the beginning of the first cycle:. This is shown in the diagram in the problem statement.'''
import os

def strangeCounter(t):
    initNum = 3
    cycleTime = 3

    while t > cycleTime:
        initNum *=2
        cycleTime += initNum

    return cycleTime - t + 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)

    fptr.write(str(result))
    fptr.close()
