import scipy.stats as st

#
# print(st.norm.ppf(.95))
# print(st.norm.cdf(1.64))

k = 8.04 / 5.5 * 1
r = st.norm.cdf(k) - st.norm.cdf(-k)
print(r)

s = st.t.cdf(k, 15) * 2 - 1
print(s)

standrds = [0.5,
            0.5398,
            0.5793,
            0.6179,
            0.6554,
            0.6915,
            0.7257,
            0.7580,
            0.7881,
            0.8159,
            0.8413,
            0.8643,
            0.8849,
            0.9032,
            0.9192,
            0.9332,
            0.9452,
            0.9554,
            0.9641,
            0.9713,
            0.9772,
            0.9821,
            0.9861,
            0.9893,
            0.9918,
            0.9938,
            0.9953,
            0.9965,
            0.9974,
            0.9981,
            0.9987,
            0.9990,
            0.9993,
            0.9995,
            0.9997,
            ]
for i in range(0, 35):
    print(st.norm.cdf(i / 10) - standrds[i])
