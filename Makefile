admin:
	python3 manage.py createsuperuser --username admin --email admin@gmail.com

mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

install-req:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt

freeze-req:
	pip3 freeze > requirements.txt

export-req:
	poetry export -f requirements.txt --output requirements.txt --without-hashes

run:
	python3 manage.py runserver 127.0.0.1:8000