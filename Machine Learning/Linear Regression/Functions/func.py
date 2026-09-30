import numpy as np

def compute_error_for_line_given_points(b, m, points):
    totalError = 0

    for i in range(0,len(points)):
        x = points[i,0]
        y = points[i,1]
        totalError += (y-((m*x) + b))**2

    return totalError/len(points)

def step_gradient(b, m, points, learning_rate):
    gradient_b = 0
    gradient_m = 0

    for i in range(len(points)):
        x = points[i,0]
        y = points[i,1]

        gradient_m += 2/len(points) * -x * (y-(m*x + b))
        gradient_b += 2/len(points) * -(y-(m*x + b))

    new_b = b -(learning_rate * gradient_b)
    new_m = m -(learning_rate * gradient_m)

    return [new_b, new_m]


def gradient_descent_runner(points,starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m

    for i in range(num_iterations):

        b, m = step_gradient(b, m, np.array(points),learning_rate)

    return [b,m]
