"""
Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

0
1
4
Input Format

The first and only line contains the integer, .

Constraints


Output Format

Print  lines, one corresponding to each .

Sample Input 0

5
Sample Output 0

0
1
4
9
16
Language
Python 3

More
1234567
if __name__ == '__main__':
    n = int(input())
i=0
while i<n:
    print(i**2)
    i=i+1

Line: 7 Col: 1

Submit Code

Run Code

Upload Code as File

Test against custom input
Blog
"""
