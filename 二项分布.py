import numpy as np

# normal = np.random.normal(1,100,25)
# print(normal)

y = []
s = 10
e = 100
g = 10

for i in range(s, e, g):
    bio_1 = np.random.binomial(10, 0.5, i)
    bio_2 = np.random.binomial(100, 0.5, i)

    bio_2 = bio_1
    f = (bio_1 - np.average(bio_1)) * (bio_2 - np.average(bio_2))

    # print(f)
    y.append(np.sum(f) / len(f))
    print(bio_1)
    print(bio_2)
    print(np.var(bio_1))
    print(np.cov(bio_1, bio_2))
    print(np.sum(f) / (len(f)-1))
#
# plt.plot(range(s, e, g), y)
# plt.show()
