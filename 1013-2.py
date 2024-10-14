import numpy as np
A=np.array([[1,2,3],[4,5,6]])
B=np.array([[4,5,9],[1,4,7]])
common_elements=np.intersect1d(A,B)
print(common_elements)
