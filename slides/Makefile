
default: figures pdfs

figures: poisson.py height.py
	python poisson.py
	python height.py
	python transit-data.py

pdfs: *.tex
	pdflatex -shell-escape probability
	pdflatex -shell-escape probability
	pdflatex -shell-escape distributions
	pdflatex -shell-escape distributions
	pdflatex -shell-escape parameter-estimation
	pdflatex -shell-escape parameter-estimation
	pdflatex -shell-escape metropolis
	pdflatex -shell-escape metropolis



