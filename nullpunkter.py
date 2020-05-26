import sys

# Test function and derivative
def f(x):
    return 9 - x*(x-10)

def fder(x):
    return -2*x + 10

# Newton–Raphson method for finding 0s
def newton(guess: float, debug=False):
    while abs(f(guess)) > 0.01:
        next_guess = guess - f(guess) / fder(guess)
        guess = next_guess
        if debug:
            print(guess);
    return guess

# Bisection method for finding 0s
def bisection(guess: float, debug=False):
    # Handle initial conditions
    a = guess if guess < 0 else 0
    b = guess if guess > 0 else 0
    c = (a + b) / 2

    # Shrink range iteratively
    while abs(f(c)) > 0.01:
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c
        c = (a + b) / 2
        if debug:
            print(c)

    return (a + b) / 2

# Handle system arguments
arg = float(sys.argv[2])
debug = len(sys.argv) > 3 and sys.argv[3] == "debug";

# Print based on first system argument /newton|\w+ \d+/
if (sys.argv[1] == "newton"):
    print(newton(arg, debug));
else:
    print(bisection(arg, debug));
