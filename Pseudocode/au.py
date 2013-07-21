def au(state, formula):
    # If the state is already marked and its labels contain the formula then
    # formula holds in `state`. Otherwise we have found a circle
    # where`formula.second_subformula` is `false` or we have found a
    # successor state where formula.first_subformula` is `false`. In both
    # cases the formula does not hold in `state`
    if marked[state]:
        return True if formula in state.labels else False

    # Check if we can immediately answer the question if
    #       A [formula.first_subformula U formula.second_subformula]
    # holds in `state`
    if formula.second_subformula in state.labels:
        labels.add(formula)
        return True
    if not formula.first_subformula in state.labels:
        return False

    # For all successors excluding the current state
    for successor in state.neighbours.difference({state}):
        # For some successors state, formula does not hold
        if not au(successor, formula):
            return False
    # For all successors state `formula` holds
    return True
