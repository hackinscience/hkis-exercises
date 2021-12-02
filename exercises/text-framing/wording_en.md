In this exercise, we'll frame text.

To frame text, we'll first define what's a frame, by using a
[dataclass](https://docs.python.org/3/library/dataclasses.html):

```python
@dataclass
class Frame:
    top: str = "-"
    left: str = "|"
    bottom: str = "-"
    right: str = "|"
    top_left: str = "+"
    top_right: str = "+"
    bottom_left: str = "+"
    bottom_right: str = "+"
```

We'll then be able to easily create new frames:

```python
fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")
```

The prototype of your function should be:

```python
def frame_text(text: str, frame: Frame) -> str:
    ...
```

Meaning your function has to accept two parameters: some text, and the frame to apply.

Your function should return the framed text.


## Examples

```python
print(frame_text(f"It is {datetime.now():%H:%I:%S}.", fancy_frame))
```
Should give:
```
╭───────────────╮
│It is 16:04:37.│
╰───────────────╯
```

Beware, your function should **return** the framed text, but not print
it, this will allow you to compose frames:

```python
text = f"It is {datetime.now():%H:%I:%S}."
text = frame_text(text, invisible_frame)
text = frame_text(text, fancy_frame)
```

gives :
```
╭─────────────────╮
│                 │
│ It is 16:04:56. │
│                 │
╰─────────────────╯
```

Beware of multi-line text:

```python3
text = """It is 16h19.
And it's raining."""
text = frame_text(text, fancy_frame)
text = frame_text(text, fancy_frame)
print(text)
```

should give:

```
╭───────────────────╮
│╭─────────────────╮│
││It is 16h19.     ││
││And it's raining.││
│╰─────────────────╯│
╰───────────────────╯
```
