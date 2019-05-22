import math

equation_1 = lambda x: x - 5
derivative_1 = lambda x: 1

equation_2 = lambda x: math.e**(2*x - 4) - x
derivative_2 = lambda x: 2*math.e**(2*x - 4) - 1

equation_3 = lambda x: x**2
derivative_3 = lambda x: 2*x

equation_4 = lambda x: x*(math.e**(-x**2))
derivative_4 = lambda x: math.e**(-x**2) + (-2*x**2)*(math.e**(-x**2))


def same_sign(a, b):
    return a*b > 0


def roots_newton(eq, deriv, guess, tolerance):

    # Set erros, iteration, old X values
    error = math.inf
    iteration = 0
    x_old = guess

    while tolerance < error:
        iteration = iteration + 1
        # Set new X value
        x_new = x_old - eq(x_old)/deriv(x_old)
        # Calculate the new error
        error = abs((x_new - x_old)/x_new)
        # Reset the old X value
        x_old = x_new

        if iteration > 100:
            break

    # Calculate the Y value
    yval = eq(x_old)

    return round(x_old, 5), round(yval, 5)

# ----------


def roots_bracket(eq, interval, tolerance):

    # Return error if interval has same sign
    if same_sign(eq(interval[0]), eq(interval[1])):
        error = 0
        mid = math.inf/math.inf
        fmid = math.inf/math.inf
    else:
        error = math.inf

    # Set iteration and upper/lower values
    iteration = 0
    lpx = interval[0]
    upx = interval[1]

    # Set previous value to midpoint on first iteration
    prev = math.inf

    # Run until tolerance parameter is met
    while tolerance < error:
        iteration = iteration + 1
        # Lower Y value
        lpy = eq(lpx)
        # Midpoint between upper and lower X value
        mid = (lpx + upx)/2
        # Y value for midpoint
        fmid = eq(mid)

        # If lower Y has the same sign as Y mid, then set lower X to mid, otherwise set upper X to mid
        if same_sign(fmid, lpy):
            lpx = mid
        else:
            upx = mid

        # Set new error
        if iteration > 1:
            error = abs(prev - mid)/abs(prev)

        prev = mid

    return round(mid, 5), round(fmid, 5)


print('Newton - E1 Root at:', roots_newton(equation_1, derivative_1, -1.5, 10**-6))
print('Newton - E2 Root at:', roots_newton(equation_2, derivative_2, -1.5, 10**-6))
print('Newton - E2 Root at:', roots_newton(equation_2, derivative_2, 2, 10**-6))
print('Newton - E3 Root at:', roots_newton(equation_3, derivative_3, -2, 10**-6))
print('Newton - E4 Root at:', roots_newton(equation_4, derivative_4, 0.8, 10**-6),'\n')

print('Bracket - E1 Root at:', roots_bracket(equation_1, [0, 6], 10**-6))
print('Bracket - E2 Root at:', roots_bracket(equation_2, [1, 10], 10**-6))
print('Bracket - E2 Root at:', roots_bracket(equation_2, [-1, 2], 10**-6))
print('Bracket - E3 Root at:', roots_bracket(equation_3, [-5, 4], 10**-6))
print('Bracket - E4 Root at:', roots_bracket(equation_4, [-2, 3], 10**-6))