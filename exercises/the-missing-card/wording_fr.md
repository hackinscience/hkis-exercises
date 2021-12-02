Write a function named `missing_card` that given a card game returns
the (single) missing card name.

The card game will be given as a single string of space-separated cards names.

A card is represented by its color and value, the color being in
`{"S", "H", "D", "C"}` and the value being in `{"2", "3", "4", "5", "6", "7",
"8", "9", "10", "J", "Q", "K", "A"}`, for a total of 52 possibilities.

You'll always be given 51 cards, and you have to return the missing one.


## Example

```python
print(
    missing_card(
        "S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA "
        "H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA "
        "D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA "
        "C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK"
    )
)

```

should print `CA` (beware, your function should `return`, in my
example I used `print` to print it).
