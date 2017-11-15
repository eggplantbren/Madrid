
default: figures pdfs

figures: poisson.py height.py
	python poisson.py
	python height.py
	python transit-data.py

pdfs: *.tex
	pdflatex -shell-escape 1-probability
	pdflatex -shell-escape 1-probability
	pdflatex -shell-escape 2-distributions
	pdflatex -shell-escape 2-distributions
	pdflatex -shell-escape 3-parameter-estimation
	pdflatex -shell-escape 3-parameter-estimation
	pdflatex -shell-escape 4-metropolis
	pdflatex -shell-escape 4-metropolis
	pdflatex -shell-escape 5-nested-sampling
	pdflatex -shell-escape 5-nested-sampling
	pdflatex -shell-escape 6-hierarchical-models
	pdflatex -shell-escape 6-hierarchical-models
	rm *.aux *.log *.nav *.out *.snm *.toc *.vrb




