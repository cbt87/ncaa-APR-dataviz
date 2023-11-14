#make everything
all: clean_data q1 q2 q3 EDA

clean_data: data/
	python -B clean_data.py

q1:
	python -B question_1.py

q2:
	python -B question_2.py	

q3:
	python -B question_3.py

EDA:
	python -B mean_APR_change.py