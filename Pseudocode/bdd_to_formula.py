#!/usr/bin/env python3
# coding=utf-8

# -----------------------------------------------------------------------------
# 	Support for generating formulas from a given BDD.
#
# 	Version: 1
# 	Date:    2013-07-13
# 	Author:  René Schwaiger (sanssecours@f-m.fm)
# -----------------------------------------------------------------------------

# -- Imports ------------------------------------------------------------------

from bdd import Node, Terminal  # noqa

# -- Functions ----------------------------------------------------------------


def bdd_to_formula(node, previous_variables=None):
    """Convert a binary decision diagram to a boolean formula.

    This function creates a formula in disjunctive normal form. For every path
    to the terminal “1”, it creates a subformula, containing the variables of
    this path.

    previous_variables - A list containing the variables of the BDD nodes
                         already visited.

    Examples:

        >>> terminal_false = Terminal(False)
        >>> terminal_true = Terminal(True)
        >>> node_a2 = Node(terminal_false, terminal_true, 'a2')
        >>> node_b1_1 = Node(node_a2, terminal_false, 'b1')
        >>> node_b1_2 = Node(terminal_false, node_a2, 'b1')
        >>> node_a1 = Node(node_b1_1, node_b1_2, 'a1')
        >>> bdd_to_formula(node_a1)
        '(¬a1∧¬b1∧a2)∨(a1∧b1∧a2)'

    """
    # At the end of the path (terminal node)
    if isinstance(node, Terminal):
        return (['∧'.join(previous_variables)]
                if previous_variables and node.value
                else [str(node.value)])

    # We create a formula by joining the solutions from all paths by
    # disjunction
    if not previous_variables:
        formulas = bdd_to_formula(node.low, ['¬{}'.format(node.variable)])
        formulas.extend(bdd_to_formula(node.high,
                                       ['{}'.format(node.variable)]))
        # Filter empty terms (terminal node and therefore formula is false)
        formulas = [formula for formula in formulas
                    if not (formula.startswith(str(False)))]
        solution = '∨'.join(['({})'.format(formula) for formula in formulas])
        return solution

    # Extend the variables already visited with the current variable
    variables_low = previous_variables + ['¬{}'.format(node.variable)]
    variables_high = previous_variables + ['{}'.format(node.variable)]
    formulas = bdd_to_formula(node.low, variables_low)
    formulas.extend(bdd_to_formula(node.high, variables_high))
    return formulas

if __name__ == '__main__':
    # Import and run doc-tests
    import doctest
    doctest.testmod()
