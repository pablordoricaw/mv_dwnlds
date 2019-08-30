SRC=./mv_dwnlds/mv_dwnlds.py

.PHONY: help start stop restart

help:
	@echo "Available targets:"
	@echo "- start: start the program in the background"
	@echo "- stop: kill the program running in the background"
	@echo "- restart: restart the program in the background"

start:
	python $(SRC) &

stop:
	pkill -f $(SRC)

restart: stop start
