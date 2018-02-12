# example: make deploy version=1-0-0

deploy:
	gcloud app deploy app.yaml queue.yaml --version dev --project coder-not-fighter

dev_server:
	dev_appserver.py app.yaml --admin_port=8080 --port=8000 --api_port=8081

install-reqs:
	pip install -t libs -r requirements.txt
