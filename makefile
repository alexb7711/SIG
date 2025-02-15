################################################################################
# Variables
################################################################################

##==============================================================================
# Directories
SRC_D     = SIG
TST_D     = tests
ENV_DIR   = .venv
ifneq ($(wildcard $(ENV_DIR)/bin/.),)
NOSE_DIR  = $(ENV_DIR)/bin
else
NOSE_DIR  = $(ENV_DIR)/Scripts
endif

##==============================================================================
# File Paths
ifneq ($(shell uname -s), "Linux")
BIN     = $(ENV_DIR)/bin
else
BIN     = $(ENV_DIR)/Scripts
endif
PYTHON  = python

##==============================================================================
# Makefile configuration
.PHONY: all setup install update run debug clean test help doc

################################################################################
# Recipes
################################################################################

##==============================================================================
#
all: setup update run ## Default action

##==============================================================================
#
.ONESHELL:
test: setup ## Run unit tests
	source $(BIN)/activate
	$(PYTHON) -m unittest discover -s $(TST_D) -p "test_*.py"
	$(PYTHON) -m unittest discover -s $(TST_D) -p "test_*.py"

##==============================================================================
#
.ONESHELL:
setup: ## Set up the project
	@$(PYTHON) -m venv $(ENV_DIR)
	@source $(BIN)/activate
	@pip install --upgrade pip
	@pip install .

##==============================================================================
#
.ONESHELL:
update: ## Update the virtual environment packages
	@source $(BIN)/activate
	@pip install --upgrade pip
	@pip install .

##==============================================================================
#
.ONESHELL:
run: ## Execute the program
	source $(BIN)/activate
	cd $(SRC_D)
	$(PYTHON) main.py

##==============================================================================
#
doc: ## Generate SIG documentation
	doxygen Doxyfile

##==============================================================================
#
debug: ## Enable the debugger (requires `pudb`)
	@source $(BIN)/activate  && \
	cd $(SRC_D)              && \
	python -m pudb main.py

##==============================================================================
#
clean: ## Cleanup the project
	rm -rfv $(ENV_DIR)

##==============================================================================
# https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html
help:  ## Auto-generated help menu
	@grep -P '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	sort                                                | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
