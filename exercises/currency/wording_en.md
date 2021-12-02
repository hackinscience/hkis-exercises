Write a function named `how_to_pay` taking two parameters: `amount`
and `currency`.

- `amount` is an amount to pay.
- `currency` describe the currency as a list of existing coins or banknotes.

The function should return a `dict` describing the easiest way to pay
`amount` with the given `currency`.


For example, to pay `3` with a currency having coins of `[1, 2, 5]`
you have to use one coin of `2` and one coin of `1`, so the function
should return `{2: 1, 1: 1}`.


## Usage example

```pycon
>>> euro = [1, 2, 5, 10, 20, 50, 100, 200, 500]
>>> how_to_pay(500, euro)
{500: 1}  # means: To pay 500€: give one bill of 500€
>>> how_to_pay(10, euro)
{10: 1}  # means: To pay 10€: give one bill of 10€
>>> how_to_pay(123, euro)    # To pay 123 euros:
{100: 1, 20: 1, 2: 1, 1: 1}  # give 1 bill of 100€, one bill of 20€,
                             # one coin of 2€, and one coin of 1€.
```

## Hint

It is OK to explicitly tell there's no need of a specific coin, but
not mandatory, both are good to me. I mean both are valid answers:

```python
>>> how_to_pay(1, [1, 5])
{1: 1, 5: 0}
>>> how_to_pay(1, [1, 5])
{1: 1}
```
