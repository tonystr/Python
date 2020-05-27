import matplotlib.pyplot as plt

def f(x):
    return x**2

def rectangle_method(f, a, b, n):
    """
    Integreringsfunksjonen rektangelmetoden
    @arg f: hvilken funksjon som skal integreres
    @arg a: lave grense for intervallet
    @arg b: høye grense for intervallet
    @arg n: antall rektangler
    """
    acc = 0.
    h = (b - a) / n
    for i in range(0, n):
        acc += f(a + (i * h))
    return acc * h

def trapeze_method(f, a, b, n):
    """
    Integreringsfunksjonen trapesmetoden
    @arg f: hvilken funksjon som skal integreres
    @arg a: lave grense for intervallet
    @arg b: høye grense for intervallet
    @arg n: antall rektangler
    """
    h = (b - a) / n
    acc = (f(a) + f(b)) / 2.
    for i in range(1, n):
        acc += f(a + i * h)
    return acc * h

def simpson(f, a, b, n):
    """
    Integreringsfunksjonen simpson's regel
    @arg f: hvilken funksjon som skal integreres
    @arg a: lave grense for intervallet
    @arg b: høye grense for intervallet
    @arg n: antall rektangler
    """
    h = (b - a)/n
    acc = 0.0

    x = a + h
    for i in range(1, int(n/2) + 1):
        acc += f(x)*4
        x += h*2

    x = a + h*2
    for i in range(1, int(n/2)):
        acc += f(x)*2
        x += h*2
    return (f(a) + f(b) + acc)*h/3

def average(f, a, b, n):
    """
    Integreringsfunksjon som tar gjennomsnitt av two punkter
    @arg f: hvilken funksjon som skal integreres
    @arg a: lave grense for intervallet
    @arg b: høye grense for intervallet
    @arg n: antall rektangler
    """
    h = (b - a)/n
    l = f(a)
    acc = l
    for i in range(1, n):
        nf = f(a + i*h)
        acc += (nf + l) / 2
        l = nf
    return acc * h

print("rectangle_method:", rectangle_method(f, 0, 5, 1000))
print("trapeze_method:  ", trapeze_method(f, 0, 5, 1000))
print("simpson:         ", simpson(f, 0, 5, 1000))
print("average:         ", average(f, 0, 5, 1000))
print("analytic:        ", (1 / 3) * 5**3)

# plt.plot(plx, ply)
# plt.show()
