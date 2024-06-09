import math
import numpy as np

def regression_loss_function():
    # Prompt user for the number of samples and ensure it's a numeric string
    num_samples_input = input("Input number of samples (integer number) which are generated: ")
    if not num_samples_input.isnumeric():
        # Handle the case where the input is not numeric
        print("Samples must be an integer number")
        return None

    # Prompt user for the loss function name
    loss_name = input("Input loss name (MAE|MSE|RMSE) :")

    # Check if the provided loss function is supported
    if loss_name not in ["MAE", "MSE", "RMSE"]:
        print(f"{loss_name} is not supported")
        return None

    # Generate random predictions and targets
    predict_list = np.random.uniform(0, 10, size=num_samples)
    target_list = np.random.uniform(0, 10, size=num_samples)

    # Calculate and print the loss based on the selected loss function
    if loss_name == "MAE":
        # Mean Absolute Error calculation
        loss = 0
        for i in range(num_samples):
            print(f"loss name: MAE, sample : {i}, pred = {predict_list[i]}, target : {target_list[i]}, loss : {abs(predict_list[i] - target_list[i])}")
            loss += abs(predict_list[i] - target_list[i])
        print(f"Final MAE : {loss/num_samples}")

    elif loss_name == "MSE":
        # Mean Squared Error calculation
        loss = 0
        for i in range(num_samples):
            print(f"loss name: MSE, sample : {i}, pred = {predict_list[i]}, target : {target_list[i]}, loss : {(predict_list[i] - target_list[i])**2}")
            loss += (predict_list[i] - target_list[i])**2
        print(f"Final MSE : {loss/num_samples}")

    elif loss_name == "RMSE":
        # Root Mean Squared Error calculation
        loss = 0
        for i in range(num_samples):
            print(f"loss name: RMSE, sample : {i}, pred = {predict_list[i]}, target : {target_list[i]}, loss : {math.sqrt((predict_list[i] - target_list[i])**2)}")
            loss += (predict_list[i] - target_list[i])**2
        print(f"Final RMSE : {math.sqrt(loss/num_samples)}")
