def MDnRE(y, y_hat, n, p):
    # Compute the MDnRE using the given formula
    loss = ((y**(1/n) - y_hat**(1/n))**p) / 1
    # Print the computed loss value
    print(f"Mean Difference Root Error Single Sample loss = {loss}")
