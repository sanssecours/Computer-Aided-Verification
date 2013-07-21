if formula.operator == 'AX':
    for state in kripke_structure.states:
        # If the set of neighbours where the subformula does not hold is empty
        if not {neighbour for state.neighbours
                if formula.first_subformula in neighbour.labels}:
            state.labels.add(formula)
