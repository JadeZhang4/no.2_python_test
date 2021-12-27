import random

N = 1*10**8
n = 0

for i in range(N):
    x = random.random()
    y = random.random()

    dist = x*x + y*y

    if dist < 1:
        n = n + 1

pi = 4.0 * n / N

print(pi)
