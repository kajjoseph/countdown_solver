test_eq = ["1", "0", "+", "5", "*", "1", "0","0", "/", "2", "5", "-", "2", "+", "7"]
"""
 0 1 2 3 4 5 6 7 8 9 -
[1 + 2 + 3 + 4 + 5 + 6]
"""
templates = {
	5: ["(012)34", "01(234)"],
	7: ["(012)3456", "01(234)56", "0123(456)", "(01234)56", "01(23456)", "(012)3(456)"],
	9: ["(012)345678", "01(234)5678", "0123(456)78", "012345(678)", "(01234)5678", "01(23456)78",
	"0123(45678)", "(0123456)78", "01(2345678)", "(012)3(456)78", "(012)345(678)", "01(234)5(678)",
	"(01234)5(578), (012)3(45678)"],
	11: ['(012)3456789-', '(012)3(456)789-', '(012)3(456)7(89-)', '(012)34567(89-)',
         '(012)3(45678)9-', '(012)3(456789-)',
         '(01234)56789-', '(01234)5(678)9-', '(01234)5(6789-)', '(01234)567(89-)',
         '(0123456)789-', '(0123456)7(89-)', '(012345678)9-',
         '01(234)56789-', '01(234)5(678)9-', '01(234)5(6789-)', '01(23456)789-', '01(23456)7(89-)', '01(23456789-)',
         '0123(456)789-', '0123(456)7(89-)', '0123(45678)9-', '0123(456789-)',
         '012345(678)9-', '012345(6789-)']
}


def join_equation(equation):
	joined_eq = [""]
	index = 0
	for i in equation:
		if i.isdigit():
			joined_eq[index] += i
		else:
			joined_eq.append(i)
			joined_eq.append("")
			index += 2
	return joined_eq
	
	
def add_brackets(equation):
	equation = join_equation(equation)
	eq_len = len(equation)
	if eq_len not in [5, 7, 9, 11]:
		return
	eq_list =[]
	for i in templates[eq_len]:
		bracketed_eq = ""
		for x in i:
			if x in ["(", ")"]:
				bracketed_eq += x
			else:
				try:
					bracketed_eq += equation[int(x)]
				except:
					bracketed_eq += equation[-1]
		eq_list.append(bracketed_eq)
	return eq_list
	
if __name__ == "__main__":	
	bracketed_eq = add_brackets(test_eq)
	print(bracketed_eq)
	print(len(bracketed_eq))
	