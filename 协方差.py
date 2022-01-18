import numpy as np

# 随机生成两个样本
x = np.random.randint(0, 9, 1000)
y = np.random.randint(0, 9, 1000)

# 计算平均值
mx = x.mean()
my = y.mean()

# 计算标准差
stdx = x.std()
stdy = y.std()

# 计算协方差矩阵
covxy = np.cov(x, y)
print(covxy)

# 我们可以手动进行验证
# covx等于covxy[0, 0], covy等于covxy[1, 1]
# 我们这里的计算结果应该是约等于，因为我们在计算的时候是使用的总体方差(总体方差和样本方差是稍微有点区别的)
covx = np.mean((x - x.mean()) ** 2)
covy = np.mean((y - y.mean()) ** 2)
print(covx)
print(covy)
# 这里计算的covxy等于上面的covxy[0, 1]和covxy[1, 0]，三者相等
covxy = np.mean((x - x.mean()) * (y - y.mean()))
print(covxy)

# 下面计算的是相关系数矩阵(和上面的协方差矩阵是类似的)
coefxy = np.corrcoef(x, y)
print(coefxy)
