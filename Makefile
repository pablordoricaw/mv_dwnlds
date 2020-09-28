SHELL=/usr/local/bin/zsh

CMD=python ./mv_dwnlds/mv_dwnlds.py
RUNIN=if pgrep -f "$(CMD)" > /dev/null; then true; else false; fi
NOTRUNIN=! $(RUNIN)
KILL=pkill -f

ENV=mv_dwnlds
CONDA_BASE=/Users/pablordoricaw/anaconda3
SOURCE=source $(CONDA_BASE)/etc/profile.d/conda.sh
ACTIVATE= conda activate $(ENV)
DEACTIVATE=conda deactivate

.PHONY: help start stop restart clean

help:
	@echo "Available targets:"
	@echo "- start: start the program in the background"
	@echo "- stop: kill the program running in the background"
	@echo "- restart: restart the program in the background"
	@echo "- status: display if the program is running in the background"
	@echo "- clean: remove all directories and files in Descargas"

start:
	@if $(NOTRUNIN); then \
	$(SOURCE) && \
	$(ACTIVATE) && \
	$(CMD) & \
	echo -e "Started $(CMD) in the background..."; \
else \
	echo "$(CMD) is already running in the background..."; \
fi;

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

clean:
	@echo "Removing all directories and files in Descargas"
	@rm -rf /Users/pablordoricaw/Descargas/*
	@echo -e "Listo \c"
	@printf '\342\234\224\n' | iconv -f UTF-8
