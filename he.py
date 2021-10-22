# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt
import numpy as np
re = 30
x  = np.arange(0,2.0,0.01)
y1 = re*(1-x)
y2 = re/(1+2*x)
line1 = plt.plot(x,y1)
line2 = plt.plot(x,y2)
plt.setp(line1,linewidth=2,color='r')
plt.setp(line2,linewidth=2,color='b')
plt.show()
