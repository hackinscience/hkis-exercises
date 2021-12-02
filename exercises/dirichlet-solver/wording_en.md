Let's play a game.

## Rules

We'll play with squares. We'll call them Dirichlet squares.

They respect one, and only one rule:

> Each cell contains the mean of the 4 surrounding cells.

like in:

```text
  8
4 6 9
  3
```

Here: `(3 + 4 + 8 + 9) / 4 == 6`.

Got the rule? Let's look at the following 3×3 square:

```text
  2 5 8
0 2 4 6 9
0 2 3 3 0
0 3 3 3 0
  7 3 6
```

(Yes, I added numbers *outside of the square* in order to check every cell in
the 3×3 square complies with the rule.)

The cells can only contain **positive integers** (`0` is allowed). The
values must be exact and not rounded.


## The game

So what's the game? The game is, I'll give you squares with holes
(like a Sudoku) and you'll have to fill them:


```text
  7 9 9
0       9
9       8
0       4
  6 0 9
```

(I'll always provide the whole border an nothing inside the actual square.)


## The exercise

You'll provide a `dirichlet_square_solver` function, taking a single
argument: a numpy array. You function will modify the array **in
place**, filling the blanks (materialized as `-1`), and return
nothing.

For the last example here's what I expect:

```python
import numpy as np

square = np.array(
    [[0,  7,  9,  9, 0],
     [0, -1, -1, -1, 9],
     [9, -1, -1, -1, 8],
     [0, -1, -1, -1, 4],
     [0,  6,  0,  9, 0]],
    dtype=int)
dirichlet_square_solver(square)
print(square)
# Should give:
# [[0 7 9 9 0]
#  [0 5 7 8 9]
#  [9 6 6 7 8]
#  [0 4 4 6 4]
#  [0 6 0 9 0]]
```

## Bonus

To do on your computer when you have the solver:

Build a huge numpy array, like 2000×6000, keep all values at 0 except
for some big "hot" points or strips around it.

Solve it...

Display it using
[matplotlib.imshow](https://matplotlib.org/3.2.1/api/_as_gen/matplotlib.pyplot.imshow.html),
choose the color palette with blue for values around 0 and red for big
values.

It should remind you a metal plate you heat up on some places, and
it's the representation of the heat propagation in the plate.

For me, when "heating" small sections at the top of a 600×800 grid, it
looks like [this](https://mdk.fr/dirichlet.png).
