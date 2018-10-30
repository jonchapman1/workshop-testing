import numpy as np
from mysoftware import *

for i in range(2, 8):
    h = 10**(-i)
    print(h,abs(CentralDifference(np.sin,0.0,h)-1.0))
 
