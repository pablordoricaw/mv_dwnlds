
PLIST=python ./mv_dwnlds/plist.py

.PHONY: help load unload status

help:
	@echo "Available targets:"
	@echo "- load: load agent"
	@echo "- unload: unload agent"
	@echo "- restart: unload + load agent"
	@echo "- status: launchctl list | grep <agent>"
	@echo "- rm: unload + rm agent plist file"

load:
	@$(PLIST) -l
	@echo "Loaded agent"

unload:
	@$(PLIST) -u
	@echo "Unloaded agent"

restart: unload load

status:
	@$(PLIST) --status

rm: unload
	@$(PLIST) --rm