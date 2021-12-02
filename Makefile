CHECKS = exercises/*/check.py

check.pot: $(CHECKS)
	xgettext --from-code UTF-8 --default-domain=check --output=check.pot exercises/**/*.py

check.po: check.pot
	msgmerge --update check.po check.pot
