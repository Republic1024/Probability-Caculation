import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

μ = 30  # 数学期望
σ = 2  # 方差
x = μ + σ * np.random.normal(0, 1, 100000)  # 正态分布
plt.hist(x, bins=100)  # 直方图显示
plt.show()
print(norm.fit(x))  # 返回极大似然估计，估计出参数约为30和2
