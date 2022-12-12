main:
	python ./main.py
	npx rimraf ./tmp

install:
	poetry install

pip-freeze:
	pip freeze > requirements.txt

pip-install:
	pip install -r requirements.txt

rimraf:
	npx rimraf ./tmp
