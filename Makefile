
install-precommit: ## Install and setup pre-commit hooks
	pre-commit install

install-poetry: ## Install packages from poetry
	poetry install

poetry-lock: ## Lock poetry packages
	poetry lock

poetry-add: ## Add a package to poetry
	poetry add $(package)

poetry-remove: ## Remove a package from poetry
	poetry remove $(package)

get-started: install-precommit install-poetry  ## Install pre-commit and poetry. Make sure you have pip installed these dependencies already!
	@echo "You're ready to go!"


 #################################################################################
 # Self Documenting Commands                                                     #
 #################################################################################

.DEFAULT_GOAL := show-help
.PHONY: show-help
show-help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'