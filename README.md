# HackInScience.org exercises mirror

This is a mirror of exercises as found in HackInScience.org database.

It is synchronized using HackInScience API via two commands, the first
one to download exercises from hackinscience.org:

    $ python ../hkis-website/scripts/fetch.py

And the second one to upload them back (it's faster to tell whicih one
to upload using the `--only` argument):

    $ python ../hkis-website/scripts/push.py --only prime


## The hierarchy

The hierarchy on the repo is the same than the one on the website, meaning:

https://www.hackinscience.org/exercises/dirichlet-solver

is stored in:

`exercises/dirichlet-solver/`.

In each exercises directory there's a bunch of files:

- `check.py`: The actual tests ran against student answers.
- `wording_en.md` and  `wording_fr.md` contains the wording (and translation) for the given exercise.
- `initial_solution.py`: The code prefilled when a student joins an exercise.
- `meta`: Other informations about the exercise (title, slug, category, author, ...)
- `pre_check.py`: Auto-generated, see `autogen_pre_check.py`.


## How to write a check.py

Write it like you'd write a unit test with pytest or unittest but
instead of just raising an AssertionError please explain what's wrong
so the student don't get stuck.

For example if you'd have to implement a test for a function returning
emojis characters containing hearts, in pytest you'd write:

```python
def test_it_contains_heart():
    for char in hearts_emojis():
        assert 'HEART' in unicodedata.name(char, '')
```

But here we'd better do:

```python
def test_it_contains_heart():
    with student_code():
        result = hearts_emojis()
    for char in result:
        charname = f"({name(char)})" if name(char, "") else ""
        fail(
            f"Why are you printing `{char}` {charname}?",
            "It does not looks like a heart to me.",
            "Your `hearts_emojis` function returned:",
            code(result),
        )
```

Always give back the full output so students can do some tests and see what change.

The `student_code`, `fail`, and `code` function comes from [correction-hepler](http://pypi.org/correction-helper).

Avoid writing a reference implementation in the `check.py`:

- It often give unhelpfull failure messages like "We do not agree, my reference implementation gives X for Y while your implementation gives X'".
- The checks are public, so you can bet someone will just copy-paste from here.


### Pitfalls

Beware of those common patterns of failing checks:

- Students modifying a mutable argument.
- Students returning unexpected things (functions, classes, None, instances, ints, complex, ...).


## i18n

po files are compiled to mo files on the correction servers via
[hkis-ansible](https://framagit.org/hackinscience/hkis-ansible).

To work on translations:

- run `make` to update the `.po` file.
- Translate the `.po` file (in `locales/fr/LC_MESSAGES/`)


## Testing

To test the check stability we use a small set of real world answers (fetched via the API), during the test, the answers that were passing before are expected to still pass, and the ones failing before are expected to fail again.

We can choose which answer is to be tested by flagging it as `safe` in the admin (beware to proofread them before marking them as safe as the execution is **not** sandboxed during those tests).

To test everything run:

    tox -p auto

Or to check a single exercise by part of its name:

    pytest -k primes


# Licenses

The HackInScience Website uses an MIT license, most of this repo use
an MIT license too.

But exercise come from various authors an may have different licenses,
if you're an author, feel free to place a LICENSE file at the root of
your exercise directory.

Unless stated differently, exericses use a [CC BY-NC
4.0](https://creativecommons.org/licenses/by-nc/4.0/) license.
