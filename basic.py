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
#print( np.arange(10000))
# A*B , A@B A.dot(B)

A = np.arange(4).reshape(2,2)
B = np.array( [ [ 1,1 ], [2,2 ]])

print(A)
print(B)
print( A*B) # elementwise product
print( A@B) # matrix product
print( A.dot(B)) #matrix product

# random...

np.random.seed(42); F = np.random.random(3); print(F)
np.random.seed(42); F = np.random.random_sample(3); print(F)
np.random.seed(42); F = np.random.bytes(3); print(F)

np.random.seed(42);
F = np.random.random_integers(0,3); print(F)
F = np.random.random_integers(0,3); print(F)
F = np.random.random_integers(0,3); print(F)
F = np.random.random_integers(0,3); print(F)
F = np.random.permutation([1,3,5]); print(F)
F = np.random.permutation([1,3,5]); print(F)
F = np.random.permutation([1,3,5]); print(F)
F = np.random.permutation([1,3,5]); print(F)
print('------------------------')
X=np.arange(3)
F = np.random.shuffle(X); print(X)
F = np.random.shuffle(X); print(X)
F = np.random.shuffle(X); print(X)
F = np.random.shuffle(X); print(X)


X=np.arange( 0,10,3 )

N = np.random.choice(X); print(N)


#ndarray method elements
#sum, min, max ,cumsum

print( '------------- some method.. ----------------')

a=np.arange(1,11)
print('sum is:', a.sum() )
print('min is :', a.min() )
print('max is :', a.max() )

a=np.arange(1,11).reshape(2,5)
print(a)

print('for axis 0 sum is:', a.sum(axis=0) )
print('for axis 0 sum is:', a.sum(axis=1) )

print('-----------------------------------------------')
a=np.arange(1,31).reshape(2,5,3)
print(a)

print('for axis 0 sum is:', a.sum(axis=0) )
print('for axis 1 sum is:', a.sum(axis=1) )
print('for axis 2 sum is:', a.sum(axis=2) )

print('for axis 0 cumsum is:\n', a.cumsum(axis=0) )
print('for axis 1 cumsum is:\n', a.cumsum(axis=1) )
print('for axis 2 cumsum is:\n', a.cumsum(axis=2) )



print ( '------------- indexing slicing iterating-----------')

a = np.arange(10)**3
print( a )

print( a[0:6:2 ])
print( a[:6:2 ])

print( a[::-1])


def f(x,y):
    return  10*x + y

print ( f(1,1 ) )

b=np.fromfunction(f,(2,3),dtype=np.int32)
print(b)
print( b[1,1])
print( b[0:2,1] )
print( b[:,1] )
print( b[1,:] )

print( b[0:2,1:3] )
print( b[-1] )
print( b[-1,:] )


for i_row in b:
    print(i_row)


for i_elem in b.flat:
    print(i_elem)
