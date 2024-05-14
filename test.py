import numpy as np

a = np.arange(6).reshape(-1, 1)
b = np.arange(6).reshape(-1, 1)
c = a[b < 3]
print(c.shape)
