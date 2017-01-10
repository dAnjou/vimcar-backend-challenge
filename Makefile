VC_APP ?= vc/main.py
VC_HOST ?= 127.0.0.1
VC_PORT ?= 5000
VC_ENV ?= env
VC_IMAGE ?= vc
VC_CONTAINER ?= vc
VC_FLASK ?= FLASK_APP=$(VC_APP) $(VC_ENV)/bin/flask

dev_init:
	python3 -m venv $(VC_ENV)
	$(VC_ENV)/bin/pip install -r requirements.txt

dev_initdb:
	$(VC_FLASK) initdb

dev_dropdb:
	$(VC_FLASK) dropdb

dev_populatedb:
	$(VC_FLASK) populatedb

dev_recreatedb: dev_dropdb dev_initdb dev_populatedb

dev_server:
	$(VC_FLASK) run --host $(VC_HOST) --port $(VC_PORT)

docker_image:
	docker build --tag $(VC_IMAGE) .

docker_run: docker_image
	docker run --rm --name $(VC_CONTAINER) -p $(VC_PORT):5000 $(VC_IMAGE)
