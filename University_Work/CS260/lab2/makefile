PYTHON = python3
VIEWER = less

.PHONY: clean run view other_run

run :  makeChart
	$(PYTHON) makeChart.py
run :  prob1
	$(PYTHON) prob1.py
run :  prob2
	$(PYTHON) prob2.py

view : time	
	- $(VIEWER) data.out

view : data.out
	
	- $(VIEWER) prob1.py
	- $(VIEWER) prob2.py


