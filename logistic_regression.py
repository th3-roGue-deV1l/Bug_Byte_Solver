import numpy as np
import math

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def compute_cost(X, y, w, b, lambda_ = 1):
    """
    Compute cost for logistic regression:
    X: input features
    y: target values
    w: weights
    b: bias
    lambda_: regularization parameter
    """

    # Number of samples
    m = X.shape[0]
    cost = 0

    for i in range(m):
        z = np.dot(w, X[i]) + b
        f_wb = sigmoid(z)
        cost += -y[i]*np.log(f_wb) - (1-y[i])*np.log(1-f_wb)
    total_cost = cost/m
    #+ lambda_/2 * np.dot(w, w)
    return total_cost

def compute_gradient(X, y, w, b, lambda_ = None):
    """
    Compute gradient for logistic regression
    X: input features
    y: target values
    w: weights
    b: bias
    lambda_: regularization parameter
    """
    m = X.shape[0]
    grad_w = np.zeros(X.shape[1])
    grad_b = 0

    for i in range(m):
        z = np.dot(w, X[i]) + b
        f_wb = sigmoid(z)
        grad_w += (f_wb - y[i]) * X[i]
        grad_b += f_wb - y[i]

    grad_w /= m
    grad_b /= m
    #+ lambda_ * w
    return grad_w, grad_b


def logistic_regression(X, y, w_in, b_in, num_steps, learning_rate, compute_cost, compute_gradient, lambda_ = None):
    """
    Compute logistic regression:
    X: input features
    y: target values
    w_in: initial weights
    b_in: initial bias
    num_steps: number of steps
    learning_rate: learning rate
    compute_cost: function to compute cost
    compute_gradient: function to compute gradient
    lambda_: regularization parameter
    """
    m = X.shape[0]

    J_history = []
    w_history = []

    for i in range(num_steps):
        cost = compute_cost(X, y, w_in, b_in, lambda_)
        grad_w, grad_b = compute_gradient(X, y, w_in, b_in, lambda_)
        w_in -= learning_rate * grad_w
        b_in -= learning_rate * grad_b

        J_history.append(cost)
        w_history.append(w_in)

        if i% math.ceil(num_steps / 10) == 0  or i == (num_steps - 1):
            print(f"Step {i}, Cost {cost}")
