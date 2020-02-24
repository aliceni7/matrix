"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    string = ""
    for row in range ( len( matrix[0] ) ):
        for column in matrix:
            string += str(column[row]) + "  "
        string += "\n"
    print( string )

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for column in range ( len( matrix ) ):
        for row in range ( len ( matrix[column] ) ):
            if ( column == row ):
                matrix[column][row] = 1.0
            else:
                matrix[column][row] = 0.0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = m2
    for a in range( len ( m2[0] ) ):
        for b in range( len (m1) ):
            ans = 0
            for c in range( len (m2) ):
                ans += temp[c][a] * m1[b][c]
            m2[b][a] = ans




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( r )
    return m
