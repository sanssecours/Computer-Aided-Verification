# -----------------------------------------------------------------------------
# 	Generate PDFs from the XeLaTeX files in the current folder
#
# 	Version: 4
# 	Date:    2013-07-21
# 	Author:  René Schwaiger (sanssecours@f-m.fm)
# -----------------------------------------------------------------------------

.PHONY: code2latex doc

# -- Variables ----------------------------------------------------------------

BDD_ISOMORPHISM = Pseudocode/bdd.py
BDD_TO_FORMULA  = Pseudocode/bdd_to_formula.py

# -- Rules --------------------------------------------------------------------

run: check_code doc

check_code:
	flake8 --exit-zero --max-complexity=10 $(BDD_ISOMORPHISM) $(BDD_TO_FORMULA)
	env $(BDD_ISOMORPHISM) && env $(BDD_TO_FORMULA)

# Remover auto generated files
clean:
	latexmk -C
	rm -r Code

# Generate the documentation
doc: code2latex
	latexmk -xelatex *.tex

# Convert sample code to (Xe)LaTeX code
code2latex:
	Utilities/convert_code_to_tex.sh
