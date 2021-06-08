# Latin-square
A Latin square design is the arrangement of t treatments, each one repeated t times, in such a way that each treatment appears exactly one time in each row and each column in the design. We denote by Roman characters the treatments. Therefore the design is called a Latin square design. This kind of design is used to reduce systematic error due to rows (treatments) and columns.
A Latin Square is a n x n grid filled by n distinct numbers each appearing exactly once in each row and column. Given an input n, we have to print a n x n matrix consisting of numbers from 1 to n each appearing exactly once in each row and each column.
Examples : 
 

Input: 3
Output:  1 2 3
         3 1 2 
         2 3 1

Input: 5
Output:  1 2 3 4 5
         5 1 2 3 4
         4 5 1 2 3 
         3 4 5 1 2
         2 3 4 5 1
 

Recommended: Please try your approach on {IDE} first, before moving on to the solution.
Did you find any pattern in which the number is stored in a Latin Square? 
 

In the first row, the numbers are stored from 1 to n serially.
In the second row, the numbers are shifted to the right by one column. i.e, 1 is stored at 2nd column now and so on.
In the third row, the numbers are shifted to the right by two columns. i.e, 1 is stored at 3rd column now and so on.
We continue the same way for the remaining rows.
Note: There may be more than one possible configuration of a n x n Latin square.
