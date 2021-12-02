CHECKS = exercises/*/check.py

locale/fr/LC_MESSAGES/check.po: locale/check.pot
	msgmerge --update $@ $<

locale/check.pot: $(CHECKS)
	xgettext --from-code UTF-8 --default-domain=check --output=$@ exercises/**/*.py
