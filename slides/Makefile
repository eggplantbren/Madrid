
default: figures pdfs

figures: poisson.py height.py
	python poisson.py
	python height.py

pdfs: *.tex
	pdflatex -shell-escape probability
	pdflatex -shell-escape probability
	pdflatex -shell-escape distributions
	pdflatex -shell-escape distributions

