Dans cet exercice, on va encadrer du texte.

Pour encadrer du texte, on va définir ce qu'est un cadre, pour ça on
va utiliser une
[dataclass](https://docs.python.org/3/library/dataclasses.html) :

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

On peut ainsi facilement créer de nouveaux cadres :

```python
fancy_frame = Frame("─", "│", "─", "│", "╭", "╮", "╰", "╯")
invisible_frame = Frame(" ", " ", " ", " ", " ", " ", " ", " ")
```

Le prototype de votre fonction doit être :

```python
def frame_text(text: str, frame: Frame) -> str:
    ...
```

C'est à dire que votre fonction doit accepter deux paramètres : du
texte, et son cadre. La fonction doit encadrer le texte donné avec le
cadre donné.

Par exemple :

```python
print(frame_text(f"Il est {datetime.now():%H:%I:%S}.", fancy_frame))
```
Doit donner :
```
╭────────────────╮
│Il est 16:04:37.│
╰────────────────╯
```

Attention, votre fonction doit **renvoyer** le texte, mais ne pas
l'afficher, ça permet de composer des cadres :

```python
texte = f"Il est {datetime.now():%H:%I:%S}."
texte = frame_text(texte, invisible_frame)
texte = frame_text(texte, fancy_frame)
```

donne :
```
╭──────────────────╮
│                  │
│ Il est 16:04:56. │
│                  │
╰──────────────────╯
```

Attention au texte multi-ligne :

```python3
texte = """Il est 16h19.
Et il ne fait pas beau."""
texte = frame_text(texte, fancy_frame)
texte = frame_text(texte, fancy_frame)
print(texte)
```

doit donner :

```
╭─────────────────────────╮
│╭───────────────────────╮│
││Il est 16h19.          ││
││Et il ne fait pas beau.││
│╰───────────────────────╯│
╰─────────────────────────╯
```
