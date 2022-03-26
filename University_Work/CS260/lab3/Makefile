
PYTHON = python3
VIEWER = less

.PHONY: prob1 prob2 prob3 clean

prob1 :
	$(PYTHON) prob1.py $(arg)

prob2 :
	$(PYTHON) prob2.py $(arg)

prob3 :
	$(PYTHON) prob3.py $(arg)
	gnuplot < plot-instructions
	display plot.png

clean :
	- \rm *.pyc >/dev/null 2>&1
	- \rm *.png >/dev/null 2>&1
	- \rm *.out >/dev/null 2>&1
 
