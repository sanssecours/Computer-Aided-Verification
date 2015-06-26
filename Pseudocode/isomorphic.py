def is_same_type(vertex1, vertex2):
    """Check if two BDDs have the same type.

    Arguments:

        [vertex1] The root of the first BDD
        [vertex2] The root of the second BDD

    Returns: ``bool``

    """
    return is_terminal(vertex1) == is_terminal(vertex2)


def isomorphic(vertex1, vertex2):
    """Check if two BBDs are isomorphic.

    Arguments:

        [vertex1] The root of the first BDD
        [vertex2] The root of the second BDD

    Returns: ``bool``

    """
    if not is_same_type(vertex1, vertex2):
        return False

    # Both terminal
    if is_terminal(vertex1):
       return value(vertex1) == value(vertex2)

    # Both nonterminal
    if not var(vertex1) == var(vertex2):
        return False

    return isomorphic(low(vertex1), low(vertex2)) and
           isomorphic(high(vertex1), high(vertex2))
