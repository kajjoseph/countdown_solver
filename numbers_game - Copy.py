import random as rng
from time import time
from bracketify import add_brackets

operators = "+-*/"
little_nums = [str(i) for i in range(1, 11)]
little_nums *= 2
rng.shuffle(little_nums)
big_nums = ["25", "50", "75", "100"]

chosen_little = rng.sample(little_nums, 4)
chosen_big = rng.sample(big_nums, 2)
chosen_nums = chosen_big + chosen_little

target = rng.randint(101, 999)
cache = []
solved = False
count = 0
start = time()

print(f"Chosen numbers: {chosen_nums}")
print(f"Target: {target}")
while not solved:
	#count += 1
	equation = []
	temp_nums = chosen_nums.copy()
	rng.shuffle(temp_nums)
	while temp_nums:
		equation += temp_nums.pop()
		if equation not in cache:
			count += 1
			#TODO: Implement bracket support
			if eval("".join(equation)) == target:
				solved = True
				solution = eval("".join(equation))
				break
			else:
				cache.append("".join(equation))
				brackets = add_brackets("".join(equation))
				if brackets:
					for i in brackets:
						pass
		equation += rng.choice(operators)
	if not equation[-1].isdigit():
		equation.pop()
	joined_eq = "".join(equation)
	

run_time = time() - start
print(joined_eq)
print(solution)
print(f"solved in {count} attempts")
print(f"and {run_time:.05} seconds")