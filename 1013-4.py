import numpy as np
url='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
filtered_rows=iris_2d[(iris_2d[:,2]>1.5)&(iris_2d[:,0]<5.0)]
print(filtered_rows)
