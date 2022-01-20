from sympy import symbols, Eq, solve

j, l, c, m, e = symbols('j,l,c,m,e')

step1 = Eq((j + l + m + e), 17100)
step2 = Eq((j + l + c + m), 15400)
step3 = Eq((l + c + m + e), 18100)
step4 = Eq((j + c + m + e), 19600)
step5 = Eq((j + l + c + e), 18200)

print(solve((step1, step2, step3, step4, step5), (j, l, c, m, e)))
