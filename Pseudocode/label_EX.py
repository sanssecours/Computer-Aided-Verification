if formula.operator == 'EX':
    for state in kripke_structure.states:
        # If the set of neighbours where the subformula holds is not empty
        if {neighbour for state.neighbours
            if formula.first_subformula() in neighbour.labels}:
                state.labels.add(formula)
