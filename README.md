Teaching notes for Madrid winter school
=======================================

(c) 2017 Brendon J. Brewer

The workshop: https://www.cosmos.esa.int/web/esac-stats-workshop-2017

LICENSE FOR CODE: GNU General Public Licence, Version 3 (see LICENSE file)

LICENSE FOR DOCUMENTS: Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) https://creativecommons.org/licenses/by-sa/4.0/


Where everything is
===================

The _slides_ directory contains LaTeX source code for the lecture slides.
It's easy to compile them to produce PDFs:

    > cd slides
    > make

The _questions_ directory contains LaTeX source code for exercise questions.
It's easy to compile them to produce PDFs:

    > cd questions
    > make

The _nested-sampling_ submodule contains Nested Sampling and Metropolis code
in Python. If you have Anaconda, these should run without problems.
You can run one or the other of these by doing this:

    > cd nested-sampling/python
    > python plain_metropolis.py
    > python nested_sampling.py
