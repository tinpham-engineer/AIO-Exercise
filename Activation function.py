def activation_function():
    # Prompt user to input a value for X
    a = input("Input X = ")

    # Prompt user to choose an activation function
    b = input("Enter activation function (sigmoid|relu|elu): ")

    # Define the alpha constant for the ELU activation function
    alpha = 0.01

    try:
        # Attempt to convert the input value for X to a float
        a = float(a)
    except ValueError:
        # Handle the error if the input value for X is not a number
        print("X must be a number")
        return None

    # Check if the provided activation function is supported
    if b not in ("sigmoid", "relu", "elu"):
        # Print an error message if the activation function is not supported
        print(f"{b} is not supported")
        return None

    # Compute and print the result of the sigmoid activation function
    if b == "sigmoid":
        print(1 / (1 + math.exp(-a)))

    # Compute and print the result of the ReLU activation function
    if b == "relu":
        if a > 0:
            print(a)
        else:
            print(0)

    # Compute and print the result of the ELU activation function
    if b == "elu":
        if a > 0:
            print(a)
        else:
            print(alpha * (math.exp(a) - 1))
