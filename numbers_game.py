import random as rng
import time
import sys

# Initialize selection pools
operators = ['+', '-', '*', '/']
big_nums = ['25', '50', '75', '100']
little_nums = [str(i) for i in range(1, 11)] * 2
little_nums.sort(key=lambda x: int(x))

# Randomly select numbers from pools
chosen_little = rng.sample(little_nums, 4)
chosen_big = rng.sample(big_nums, 2)
chosen_nums = chosen_big + chosen_little
print(chosen_nums)
target = rng.randint(101, 999)

cache = []
nearest_equations = ''
nearest_solution = 0
nearest_solution_diff = target
attempts = 0
solved = False
start_time = time.time()

##Comment out the following to select random numbers##
chosen_nums = ['50', '75', '1', '4', '3', '6']
target = 472

print(f'Chosen numbers: {" ".join(chosen_nums)}')
print(f'Target: {target}')
print('Press CTRL + C to quit and give closeset solution\n')

try:
    while not solved:
        # TODO: Find way to add brackets to equations
        # TODO: Ensure only whole positive numbers are used in equation
        # TODO: Find smarter way of building equations
        temp_nums = chosen_nums.copy()
        rng.shuffle(temp_nums)
        equation = []
        equation_is_valid = True
        while temp_nums and equation_is_valid:
            equation += temp_nums.pop()
            joined_equation = ''.join(equation)
            if joined_equation not in cache:
                attempts += 1
                solution = eval(joined_equation)
                if solution < 0 or (type(solution) == float and not solution.is_integer()):
                    cache.append(joined_equation)
                    equation_is_valid = False
                    break
                if solution == target:
                    solved = True
                    break
                else:
                    cache.append(joined_equation)
                solution_diff = abs(solution-target)
                if solution_diff < nearest_solution_diff:
                    nearest_equation = equation
                    nearest_solution = solution
                    nearest_solution_diff = solution_diff
                    
            if len(equation) < len(''.join(chosen_nums)) + len(''.join(chosen_nums)) - 1:
                equation += rng.choice(operators)
            if attempts == 100000:
                sys.exit()
                

except KeyboardInterrupt:
    if not nearest_equation[-1].isdigit():
        nearest_equation.pop()
    run_time = time.time() - start_time
    print(f'Stopped after {run_time:.5f} seconds and {attempts} attempts')
    print(f'Nearest equation: {"".join(nearest_equation)}')
    print(f'Nearest solution: {int(nearest_solution)}')
    print(f'Difference: {int(nearest_solution_diff)}')

if solved:
    run_time = time.time() - start_time
    print(f'Equation: {joined_equation}')
    print(f'Solution: {int(solution)}')
    print(f'Completed in {attempts} attempts and {run_time:.5} seconds')
