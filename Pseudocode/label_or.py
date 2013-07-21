if formula.operator == '∨':
    for state in kripke_structure.states:
        if formula.first_subformula in state.labels and
           formula.second_subformula in state.labels:
            state.labels.add(formula)
