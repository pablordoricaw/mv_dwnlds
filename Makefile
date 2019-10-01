CMD=python ./mv_dwnlds/mv_dwnlds.py
RUNIN=if pgrep -f "$(CMD)" > /dev/null; then true; else false; fi
NOTRUNIN=! $(RUNIN)
KILL=pkill -f

.PHONY: help start stop restart

help:
	@echo "Available targets:"
	@echo "- start: start the program in the background"
	@echo "- stop: kill the program running in the background"
	@echo "- restart: restart the program in the background"
	@echo "- status: display if the program is running in the background"

start:
	@if $(NOTRUNIN); then \
	$(CMD) & \
	echo "Started $(CMD) in the background..."; \
else \
	echo "$(CMD) is already running in the background..."; \
fi

stop:
	@if $(RUNIN); then \
	$(KILL) $(CMD); \
	echo "Stopped $(CMD)"; \
else \
	echo "$(CMD) is not running..."; \
fi


restart: stop start

status:
	@if $(RUNIN); then \
	echo "$(CMD) is running in the background..."; \
else \
	echo "$(CMD) is NOT running in the background..."; \
fi


