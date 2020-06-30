import numpy as np

# create

a = np.array( [1,2,3,4])

print(a)


print( a.shape )
print( a.size )
print( a.ndim )
print( a.data )
print( a.dtype )

b=np.arange(10).reshape( 2,5 ); print(b)

c=np.linspace(0,1,9); print(c)
print( np.zeros( (2,5)))
print( np.ones( (2,5)))
print( np.empty( (2,5)))
print( np.empty_like (  b ))



# set print options
print( np.arange(10000))
import sys
np.set_printoptions(threshold=sys.maxsize)
print( np.arange(10000))

# A*B , A@B A.dot(B)

A = np.arange(4).reshape(2,2)
B = np.array( [ [ 1,1 ], [2,2 ]])

print(A)
print(B)
print( A*B) # elementwise product
print( A@B) # matrix product
print( A.dot(B)) #matrix product

