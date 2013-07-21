if formula.operator == 'EU':
    # Collect all states where the second subformula holds
    states_second_formula = [state
                             for state in kripke_structure.states
                             if formula.second_subformula in state.labels]
    # Label states and their predecessors where `formula.first_subformula`
    # holds
    for state in second_subformula:
        state.labels.add(formula)
        # For all predecessors excluding the current state
        for predecessor in state.predecessors.difference({state}):
            check_pred_eu(predecessor, formula)

def check_pred_eu(state, formula):
    if formula.first_subformula in state.labels:
        labels.add(formula)
        for predecessor in state.predecessors.difference({state}):
            check_pred(predecessor, formula)
