# Meta
[NumPy for Matlab Users](http://wiki.scipy.org/NumPy_for_Matlab_Users)

# Notes
## Basics 
* A slicing operation creates a view on the original array, which is just a way of accessing array data. Thus the original array is not copied in memory
* The transposition is a view `a.T`
* To force copy: `c = a[:: 2].copy() # force a copy` 
* numpy indexing starts from `0` while MATLAB starts from `1`
* There is no differentiation for numpy of `;` `,` as in MATLAB

## Numeric Operations 
* np `array` multiplication for matrix multiplication `a.dot(b)`
* np `matrix` multiplication for matrix multiplication `A * B`