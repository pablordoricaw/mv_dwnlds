SRC=./mv_dwnlds/mv_dwnlds.py

.PHONY: help start stop restart

help:
	@echo "Available targets:"
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

start: ## Start the program in the background
	nohup python $(SRC) &

stop: ## Kill the program running the background
	pkill -f $(SRC)

restart: ## Restart the program
	stop start
