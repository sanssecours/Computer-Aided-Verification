if formula.operator == '¬':
    for state in kripke_structure.states:
        # e.g. f = ¬g ⇒ f.first_subformula = g
        if not formula.first_subformula in state.labels:
            state.labels.add(formula)
