import numpy as np
from Functions import compute_error_for_line_given_points,gradient_descent_runner

def run():
    points = np.genfromtxt('data.csv',delimiter=',')
    learning_rate = 0.0001
    initial_m = 0
    initial_b = 0
    num_iteration = 1000

    print(f'Starting Gradient Descent at b = {initial_b}, m = {initial_m}, error = {compute_error_for_line_given_points(initial_m, initial_b, points)}')
    

    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iteration)

    print(f'Starting Gradient Descent at b = {initial_b}, m = {initial_m}, error = {compute_error_for_line_given_points(b, m, points)}')



if __name__ == '__main__':
    run()
