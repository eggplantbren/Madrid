
default: figures pdfs

figures: poisson.py
	python poisson.py

pdfs: *.tex
	pdflatex -shell-escape probability
	pdflatex -shell-escape probability
	pdflatex -shell-escape distributions
	pdflatex -shell-escape distributions

