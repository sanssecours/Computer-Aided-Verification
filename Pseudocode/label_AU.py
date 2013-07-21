if formula.operator == 'AU':
    # “Unmark” all states
    marked = {state: false for state in kripke_structure.states}
    for state in in kripke_structure.states:
        if not marked[state]:
            au(state, fomula)
