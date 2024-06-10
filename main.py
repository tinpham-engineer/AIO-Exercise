import math

def approx_sin(x, n):
    # Initialize result to store the sum of the series
    result = 0
    # Loop through n terms to approximate sine
    for i in range(n):
        calculate = (-1)**i * (x**(2*i+1) / math.factorial(2*i+1))
        # Add the i-th term to the result
        result += calculate
    # Return the approximation of sin(x)
    return result

def approx_cos(x, n):
    # Initialize result to store the sum of the series
    result = 0
    # Loop through n terms to approximate cos
    for i in range(n):
        calculate = (-1)**i * (x**(2*i) / math.factorial(2*i))
        # Add the i-th term to the result
        result += calculate
    # Return the approximation of cos(x)
    return result

def approx_sinh(x, n):
    # Initialize result to store the sum of the series
    result = 0
    # Loop through n terms to approximate sinh
    for i in range(n):
        calculate = x**(2*i+1) / math.factorial(2*i+1)
        # Add the i-th term to the result
        result += calculate
    # Return the approximation of sinh(x)
    return result

def approx_cosh(x, n):
    # Initialize result to store the sum of the series
    result = 0
    # Loop through n terms to approximate cosh
    for i in range(n):
        calculate = x**(2*i) / math.factorial(2*i)
        # Add the i-th term to the result
        result += calculate
    # Return the approximation of cosh(x)
    return result