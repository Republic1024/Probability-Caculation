delta = 2.132 * 0.12
print(10 + delta, 10 - delta)

print(10 * 0.55 / (18.75 ** 0.5) + 0.25)

# hexadecimal string
hexs = ['0AFFFF', '3F', 'CD']

# conversion
for h in hexs:
    dec = int(h, 16)

    print('Value in hexadecimal:', h)
    print('Value in decimal:', dec)
