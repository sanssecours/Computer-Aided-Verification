def rule_constant(tokens):
    constant = tokens[0]
    return BDD(constant)
