# Readme

This was another dynamic programming problem, about finding how many different sets of stairs you can make out of a given number of bricks
- a step must be at least 1 brick taller than the step below it
- steps can be arbitrarily large

Given three or four bricks, only one set is possible.
like this:

\*   
\* \*  
2 + 1 = 3


\*  
\*  
\* \*  
3 + 1 = 4

with 5 bricks there are 2 sets possible:

\*
\*                         
\*                         
\* \*                      
4 + 1 = 5                  

\*  
\* \*  
\* \*  
3 + 2 = 5

This is another dynammic programming problem, but the trick here was runtime, at least the implementation I found, required memoization to complete in time for the tests to pass.  
This means we define a lookup table (dictionary) outside of the function, and each time the function runs if we find a set we've already seen, we lookup how many sets can be made from it in the table, instead of recalculating.