import numpy as np


def divide_numbers(n):
    first_set = range(1, n//2 + 1)
    second_set = range(n//2 + 1, n + 1)
    return first_set, second_set


def calculate_coefficients(nums):
    sum_x = sum(nums)
    sum_x2 = sum(x**2 for x in nums)
    sum_y = sum(nums)
    
    return sum_x, sum_x2, sum_y


def solve_equations(sum_x, sum_x2, sum_y, n):
   
    A = np.array([[sum_x2, sum_x], [sum_x, n]])
    B = np.array([sum_x * sum_y, sum_y])
    
    a, b = np.linalg.solve(A, B)
    
    return a, b


def main(n):
 
    first_set, second_set = divide_numbers(n)
    
    sum_x1, sum_x2_1, sum_y1 = calculate_coefficients(first_set)
    sum_x2, sum_x2_2, sum_y2 = calculate_coefficients(second_set)
    
    a1, b1 = solve_equations(sum_x1, sum_x2_1, sum_y1, len(first_set))
    a2, b2 = solve_equations(sum_x2, sum_x2_2, sum_y2, len(second_set))
    
    print("First set coefficients: a1 = {:.2f}, b1 = {:.2f}".format(a1, b1))
    print("Second set coefficients: a2 = {:.2f}, b2 = {:.2f}".format(a2, b2))

# Example :
n = 10 
main(n)
