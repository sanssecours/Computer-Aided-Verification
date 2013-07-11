# -----------------------------------------------------------------------------
# 	Generate PDFs from the XeLaTeX files in the current folder
#
# 	Version: 3
# 	Date:    2013-07-11
# 	Author:  René Schwaiger (sanssecours@f-m.fm)
# -----------------------------------------------------------------------------

.PHONY: clean code2latex doc test

# -- Variables ----------------------------------------------------------------

PROGRAM = Pseudocode/bdd.py

# -- Rules --------------------------------------------------------------------

run: test
	python $(PROGRAM)

test:
	flake8 --exit-zero --max-complexity=10 .

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
