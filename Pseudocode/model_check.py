# Partition the formula `f` into its subformulas
formulas = subformulas(f) ∪ f

# Go trough all subformulas beginning with the shortest formulas
for formula_length = 2…length(f):
    for formula in [formula for formula in formulas
                    if length(formula) == formula_length]:
         label(formula)

# Check if the CTL formula `f` holds in the given state
if f in formula(state):
    return True
else:
    return False
