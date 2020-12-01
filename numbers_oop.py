import random as rng
from time import time


class App:

    templates = {
    5: ['(012)34', '01(234)'],
    7: ['(012)3456', '(012)3(456)', '(01234)56', '01(234)56', '012(3456)', '0123(456)'],
    9: ['(012)345678', '(012)3(456)78', '(012)3(45678)', '(012)345(678)',
        '(01234)5678', '(01234)5(678)', '(0123456)78',
        '01(234)5678', '01(234)5(678)', '01(23456)78', '01(2345678)',
        '0123(456)78', '0123(45678)', '012345(678)'],
    11: ['(012)3456789-', '(012)3(456)789-', '(012)3(456)7(89-)', '(012)345(678)9-', '(012)34567(89-)',
         '(012)3(45678)9-', '(012)3(456789-)',
         '(01234)56789-', '(01234)5(678)9-', '(01234)5(6789-)', '(01234)567(89-)',
         '(0123456)789-', '(0123456)7(89-)', '(012345678)9-',
         '01(234)56789-', '01(234)5(678)9-', '01(234)5(6789-)', '01(23456)789-', '01(23456)7(89-)', '01(23456789-)',
         '0123(456)789-', '0123(456)7(89-)', '0123(45678)9-', '0123(456789-)',
         '012345(678)9-', '012345(6789-)', '((012)3(456))789-']
    }
    operators = '+-/*'
    little_nums = [str(i) for i in range(1, 11)] * 2
    large_nums = ['25', '50', '75', '100']

    def __init__(self, numbers=None, target=None):
        self.numbers = numbers if numbers else self.get_random_numbers()
        self.target = target if target else rng.randint(101, 999)
        self.cache = set()
        self.solved = False
        self.equation = ''
        self.solution = 0
        self.nearest_equation = ''
        self.nearest_diff = self.target
        self.valid = True

    def loop(self):
        print(f'Chosen numbers: {self.numbers}')
        print(f'Target number: {self.target}')
        while not self.solved and self.valid:
            number_pool = self.numbers.copy()
            rng.shuffle(number_pool)
            equation = []
            equation.append(number_pool.pop())
            equation.append(rng.choice(App.operators))
            equation.append(number_pool.pop())
            str_eq = ''.join(equation)
            if solution := eval(str_eq) == target:
                self.solved = True
                self.equation = str_eq
                self.solution = solution
                break
            while number_pool:
                equation.append(rng.choice(App.operators))
                equation.append(number_pool.pop())
                if str_eq not in self.cache:
                    solution = eval(str_eq)
                    if solution == self.target:
                        self.solved = True
                        self.solution = solution
                        break
                    if solution < 0 or solution % 1:
                        self.valid = False
                        self.cache.add(str_eq)
                        break
                    if brackets := self.add_brackets(equation):
                        for bracketed_eq in brackets:
                            solution = eval(bracketed_eq)
                            if solution == self.target:
                                self.solved = True
                                self.solution = solution
                                break
    
    @staticmethod
    def add_brackets(equation):
        if len(equation) not in [App.templates.keys()]:
            return
        eq_list = []
        for i in App.templates[len(equation)]:
            bracketed_eq = ''
            for x in i:
                if x in ('(', ')'):
                    bracketed_eq += x
                else:
                    try:
                        bracketed_eq += equation[int(x)]
                    except TypeError:
                        bracketed_eq += equation[-1]
            eq_list.append(bracketed_eq)
        return eq_list
        
    @staticmethod
    def get_random_numbers():
        chosen_large = rng.sample(App.large_nums, 2)
        chosen_little = rng.sample(App.little_nums, 4)
        return chosen_large + chosen_little
