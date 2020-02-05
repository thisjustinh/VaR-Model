import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

plt.plot(norm.ppf(np.random.rand(30, 1000)))
plt.show()
