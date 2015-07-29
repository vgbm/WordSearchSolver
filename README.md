# WordSearchSolver
Python script which will scan (brute force) a word search grid for the list of search words.   
This is done in parallel, where each search word gets its own process to improve performance.

The scripts uses pairs (x,y) where:  

0 ----- x ------>
|  
|  
|  
y  
|
|
|
v

and an map of directions where (p=curr point):

0 1 2
3 p 5
6 7 8
