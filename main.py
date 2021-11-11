import math
from matplotlib import pyplot as plt

# P(x >= k)
def i_cdf(n, k, p):
    return 1-cdf(n, k-1, p)

# P(x <= k)
def cdf(n, k, p):
    return sum([pdf(n, ki, p) for ki in range(k+1)])

# P(x = k)
def pdf(n, k, p):
    return math.comb(n, k) * p**k * (1-p)**(n-k)

def i_cdf_graph(n, k, p):
    x = [ni for ni in range(n+1)]
    y = [i_cdf(xi, k, p) for xi in x]
    plt.plot(x, y)
    plt.savefig("./fig")

def main():
    i_cdf_graph(100, 1, 0.02)

if __name__ == '__main__':
    main()