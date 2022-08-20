
""" /*
Objective
This is a simple challenge to help you practice printing to stdout.
You may also want to complete Solve Me First in C++ before attempting this challenge.

We're starting out by printing the most famous computing phrase of all time!
In the editor below, use either printf or cout to print the string Hello, World! to stdout.


The more popular command form is cout. It has the following basic form:

cout<<value_to_print<<value_to_print;

Any number of values can be printed using one command as shown.

The printf command comes from C language. It accepts an optional format specification and a list of variables. Two examples for printing a string are:

printf("%s", string); printf(string);

Note that neither method adds a newline. It only prints what you tell it to.

Output Format

Print Hello, World! to stdout.

Sample Output

Hello, World!
*/
#include <iostream>
using namespace std;
int main() {
    cout<<"Hello, World!";
}
"""

# 2. input and output
""" /*
Objective
In this challenge, we practice reading input from stdin and printing output to stdout.

In C++, you can read a single whitespace-separated token of input using cin, and print output to stdout using cout. For example, let's say we declare the following variables:

string s;
int n;
and we want to use cin to read the input "High 5" from stdin. We can do this with the following code:

cin >> s >> n;
This reads the first word ("High") from stdin and saves it as string , then reads the second word ("") from stdin and saves it as integer . If we want to print these values to stdout, separated by a space, we write the following code:

cout << s << " " << n << endl;
This code prints the contents of string , a single space (), then the integer . We end our line of output with a newline using endl. This results in the following output:

High 5
Task
Read  numbers from stdin and print their sum to stdout.

Input Format

One line that contains  space-separated integers: , , and .

Constraints

Output Format

Print the sum of the three numbers on a single line.

Sample Input

1 2 7
Sample Output

10
Explanation

The sum of the three numbers is .
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int a, b, c;
    int sum_ = 0; 
    cin >> a >> b >> c ;
    sum_ = a+b+c;
    cout<<sum_;
     
    return 1;
}
"""

