import numpy as np

array1 = np.array([1,2,3,4,5])
array2 = np.array([10,11,12,13,14])

z1 = array1 + array2
z2 = array1 - array2
z3 = array1 * array2
z4 = array1 / array2

print(z1.mean())
print(z2.mean())
print(z3.mean())
print(z4.mean())

x = z1 + z2 + z3 + z4
print(x.std())


