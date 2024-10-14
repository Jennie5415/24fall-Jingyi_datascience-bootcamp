import numpy as np
A=np.array([[1,2,3],[4,5,6]])
extracted_elements=A[(A>=5)&(A<=10)]
print(extracted_elements)
