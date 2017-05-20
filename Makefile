.PHONY: test test_cov

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

lint:
	flake8 hello_world test

test_run:
	PYTHONPATH=. py.test

test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=.

test_xunit:
	PYTHONPATH=. py.test -s --cov=. --junit-xml=test_results.xml

docker_build:
	docker build -t hello-world-printer .

USERNAME=leonardust
TAG=$(USERNAME)/hello-world-printer

docker_push:
	@docker login --username $(USERNAME) --password $(PASSWORD) ; \
	docker tag hello-world-printer $(TAG); \
	docker push $(TAG); \
	docker logout;
