compose_command ?= docker-compose
docker_compose_file_path ?= infrastructure/docker/docker-compose.dev.yml
app_service ?= ioet-catalog-backend

.PHONY: help
help: ## Show this help (usage: make help)
	@echo "Usage: make [target]"
	@echo "Targets:"
	@awk '/^[a-zA-Z0-9_-]+:.*?##/ { \
		helpMessage = match($$0, /## (.*)/); \
		if (helpMessage) { \
			target = $$1; \
			sub(/:/, "", target); \
			printf "  \033[36m%-20s\033[0m %s\n", target, substr($$0, RSTART + 3, RLENGTH); \
		} \
	}' $(MAKEFILE_LIST)


.PHONY: build
build:	## Build project with docker-compose
	${compose_command} -f ${docker_compose_file_path} build

.PHONY: up
up:	## Run all services locally
	${compose_command} -f ${docker_compose_file_path} up -d

.PHONY: clean
clean:	## Remove everything
	${compose_command} -f ${docker_compose_file_path} down --volumes --remove-orphans --rmi all

.PHONY: logs
logs:	## Show logs of all services
	${compose_command} -f ${docker_compose_file_path} logs -f
	
.PHONY: dev_shell
dev_shell:	## Run a dev shell
	@${compose_command} -f ${docker_compose_file_path} exec ${app_service} bash

.PHONY: create_dev_env
create_dev_env:
	python3 -m venv .venv && \
	. .venv/bin/activate && \
	pip install poetry && \
	poetry install;

.PHONY: win_create_dev_env
win_create_dev_env:
			python -m venv .venv && \
			.venv\Scripts\activate.bat && \
			pip install poetry && \
			poetry install

.PHONY: start
start:  ## Starts the debug of the program
	bash -c ". .venv/bin/activate && . .env && uvicorn main:app --reload"

.PHONY: win_start
win_start:  ## Starts the debug of the program in windows environment
	.venv\Scripts\activate.bat && \
	.env && \
	uvicorn main:app --reload
