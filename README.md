# i18n

- make check.po
- Translate the file
- python store_po.py
- python ../hkis-website/scripts/push.py --username julien --password-file ~/.hkis_password  --only bencode


# Testing

Use:

    pytest -n auto

(which is ~3 times faster than single process pytest.)

Or to check a single exercise:

    pytest -k primes


# Gotchas

- They will modify mutable arguments given to their functions.
- They will return anything from a function: functions, classes, None, instances, ints, ...
