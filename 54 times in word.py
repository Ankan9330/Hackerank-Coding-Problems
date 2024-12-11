'''Given the time in numerals we may convert it into words, as shown below:

At , use o' clock. For , use past, and for  use to. Note the space between the apostrophe and clock in o' clock. Write a program which prints the time in words for the input given in the format described.

Function Description

Complete the timeInWords function in the editor below.

timeInWords has the following parameter(s):

int h: the hour of the day
int m: the minutes after the hour
Returns

string: a time string as described
Input Format

The first line contains , the hours portion The second line contains , the minutes portion

Constraints

Sample Input 0

5
47
Sample Output 0

thirteen minutes to six
Sample Input 1

3
00
Sample Output 1

three o' clock
Sample Input 2

7
15
Sample Output 2

quarter past seven'''
import os

def timeInWords(h, m):
    hour = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve"]
    minutes = ["o' clock", "one minute", "two minutes", "three minutes", "four minutes", "five minutes", "six minutes", "seven minutes", "eight minutes", "nine minutes", "ten minutes", "eleven minutes", "twelve minutes", "thirteen minutes", "fourteen minutes", "quarter", "sixteen minutes", "seventeen minutes", "eighteen minutes", "nineteen minutes", "twenty minutes", "twenty one minutes", "twenty two minutes", "twenty three minutes", "twenty four minutes", "twenty five minutes", "twenty six minutes", "twenty seven minutes", "twenty eight minutes", "twenty nine minutes", "half"]

    if m == 0:
        return hour[h-1] + " " + minutes[m]
    elif m <= 30:
        return minutes[m] + " past " + hour[h-1]
    else:
        return minutes[29-m] + " to " + hour[h]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())
    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result)
    fptr.close()
