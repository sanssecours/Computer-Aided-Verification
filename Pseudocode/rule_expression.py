def rule_expression(tokens):
    # Constant or variable
    if len(tokens == 1):
        return tokens[0]

    # ¬ BDD
    if len(tokens == 2):
        bdd = tokens[1]
        swap_terminals(bdd)
        return bdd

    # ( BDD )
    if tokens[0] == '(':
        return tokens[1]

    # BDD operator BDD
    operator = tokens[1]
    bdd1 = tokens[0]
    bdd2 = tokens[2]
    bdd = apply(operator, bdd1, bdd2)
    reduce(BDD)
    return BDD
