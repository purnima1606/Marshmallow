"""
Objective
Today, we're learning about a new data type: sets.

Concept

If the inputs are given on one line separated by a character (the delimiter), use split() to get the separate values in the form of a list. The delimiter is space (ascii 32) by default. To specify that comma is the delimiter, use string.split(','). For this challenge, and in general on HackerRank, space will be the delimiter.

Usage:

>> a = raw_input()
5 4 3 2
>> lis = a.split()
>> print (lis)
['5', '4', '3', '2']
If the list values are all integer types, use the map() method to convert all the strings to integers.

>> newlis = list(map(int, lis))
>> print (newlis)
[5, 4, 3, 2]
Sets are an unordered collection of unique values. A single set contains values of any immutable data type.


Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}
Sample Output

5
9
11
12
Language
Python 3

More

"""

m = int(input())
s1 = set(map(int, input().split( )))
print(s1)
n = int(input())
s2 = set(map(int, input().split()))
print(s2)
res = s1.symmetric_difference(s2)
for i in res:
    print(i)
