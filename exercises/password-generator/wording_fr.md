Build a password generator by writing a function named ``pwgen`` taking the following
parameters:

 - ``length``: the length of the generated password
 - ``with_digits``: Defaulting to True, to allow or disallow digits
 - ``with_uppercase``: Defaulting to True, to allow or disallow capital letters

`pwgen` returns a password with lowercase letters AND digits
if `with_digits == True` AND uppercase letters if `with_uppercase == True`.

When asked for a password with multiple character categories,
all categories have to be represented.
For instance, with `with_digits == True`, the password must have at least one
lowercase letter AND at least one digit.

## Hints

- Expect Moulienette to call the function many times, so avoid
using blocking calls to obtain "truly random bits", it will just
exhaust our system entropy and will take forever to check your
exercise.
