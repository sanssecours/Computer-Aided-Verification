#!/usr/bin/env python
# coding=utf-8

# -----------------------------------------------------------------------------
# 	Various code to create and operate on binary decision diagrams.
#
# 	Version: 2
# 	Date:    2013-07-12
# 	Author:  René Schwaiger (sanssecours@f-m.fm)
#
# -----------------------------------------------------------------------------

# -- Classes ------------------------------------------------------------------


class Terminal(object):
    """A terminal node of a BDD."""

    def __init__(self, value=True):
        """Initialize a new terminal node.

        Arguments:

            value - The (binary) value of the terminal node (default: True)

        """
        self.value = value

    def __eq__(self, bdd_node):
        """Compare this terminal to an other BDD node.

        Arguments:

            bdd_node - The BDD node to compare this terminal against.

        Examples:

            >>> terminal_true = Terminal()
            >>> terminal_true == Terminal(True)
            True
            >>> terminal_true == Terminal(False)
            False

        """
        try:
            # Compare two terminals
            return self.value == bdd_node.value
        except AttributeError:
            # A terminal can never be equal to a non-terminal object
            return False


class Node(object):
    """A node of a binary decision diagram."""

    def __init__(self, low, high, variable):
        """Initialize a new BDD node.

        Arguments:

            low      - The low child of the node.
            high     - The high child of the node.
            variable - The variable represented by this node.

        """
        self.low = low
        self.high = high
        self.variable = variable

    def __eq__(self, node):
        """Compare this BBD nodes to an other BDD node.

        Arguments:

            node - The BDD node to compare this node against.

        Examples:

            >>> terminal_false = Terminal(False)
            >>> terminal_true = Terminal(True)
            >>> node = Node(terminal_false, terminal_false, 'p')
            >>> node2 = Node(node, terminal_true, 'p')
            >>> node == node2
            False
            >>> node2 == Node(node, terminal_true, 'p')
            True

        """
        try:
            return (self.variable == node.variable and
                    self.low == node.low and
                    self.high == node.high)
        except AttributeError:
            return False


class BDD(object):
    """Saves data contained in a binary decision diagram."""

    def __init__(self, root):
        """Create a new BDD.

        Arguments:

            root - The root of the new BDD. This can be either a “normal” node
                   or a terminal node.

        Examples:

            >>> terminal_true = Terminal(True)
            >>> bdd = BDD(terminal_true)
            >>> BDD = Node(terminal_true, terminal_true, 'a')

        """
        self.root = root

    def isomorphic(self, bdd):
        """Check if two BDDs are isomorphic or not.

        Both BDDs for this function need to be fully reduced and have the same
        ordering. Otherwise this function will return ``False`` although the
        BDDs might in fact be isomorphic.

        Arguments:

            bdd - The BDD to compare this BDD against.

        Examples:

            >>> terminal_false = Terminal(False)
            >>> terminal_true = Terminal(True)
            >>> BDD(terminal_true).isomorphic(BDD(terminal_false))
            False
            >>> node_b1 = Node(terminal_false, terminal_false, 'b')
            >>> node_b2 = Node(terminal_false, terminal_true, 'b')
            >>> node_a1 = Node(node_b1, node_b2, 'a')
            >>> BDD(node_a1).isomorphic(BDD(terminal_false))
            False
            >>> BDD(node_a1).isomorphic(BDD(node_a1))
            True
            >>> node_a2 = Node(node_b1,
            ...                Node(terminal_true, terminal_true, 'b'),
            ...                'a')
            >>> BDD(node_a1).isomorphic(BDD(node_a2))
            False

        """
        return self.root == bdd.root


if __name__ == '__main__':
    # Import and run doc-tests
    import doctest
    doctest.testmod()
