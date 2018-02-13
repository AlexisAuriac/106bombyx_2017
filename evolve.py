def gen100(n, k):
    for i in range(1, 101):
        print(i, "%.2f" % n)
        n = n * k * (1000 - n) / 1000


def bounds(n, i0, i1):
    k = 1.00
    while k < 4:
        gen = n
        i = 0
        while i < i0:
            gen = gen * k * (1000 - gen) / 1000
            i += 1
        while i <= i1:
            print("%.2f %.2f" % (k, gen))
            gen = gen * k * (1000 - gen) / 1000
            i += 1
        k += 0.01
