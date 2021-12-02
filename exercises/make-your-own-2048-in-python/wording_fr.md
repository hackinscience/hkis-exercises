## Presentation

During this exercise you will build your own 
[2048](https://gabrielecirulli.github.io/2048/) game! 

If you never played, have some fun [here](https://gabrielecirulli.github.io/2048/) 
for a moment :)

## Introducing Numpy

There is many ways to do this, but here we will consider the game's board as a matrice
and use [numpy](http://www.numpy.org/) to program the game. 
If you installed Anaconda Python, you already have this module.

[Numpy](http://www.numpy.org/) is a Python module introducing 
[matrices](https://en.wikipedia.org/wiki/Matrix_(mathematics)) 
and many other linear algebra data types and functions. 
It is widely used for scientific computing, area in which Python is 
excelling.

If you're familiar with Matlab or Octave, have a look at 
[this page](http://mathesaurus.sourceforge.net/matlab-numpy.html) which compare 
most famous operations form one language to the other.

Here are a few examples:

!!! note
    By convention, we import numpy like this to avoid to have to type `numpy` 
    each time we want to use it in our program.


```python
>>> import numpy as np
```

Initiate a 4x4 matrice of zeros considered as integers:

```python
>>> m = np.zeros((4,4), dtype=int)
>>> print(m)
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
```

Changing the value of one or many elements:

```python
>>> m[3,2] = 1
>>> print(m)
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]
 [0 0 1 0]]
>>> m[3,:] = 1
>>> print(m)
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]
 [1 1 1 1]]
```

Getting the position of specific values:
```python
>>> np.where(m == 1)
(array([3, 3, 3, 3]), array([0, 1, 2, 3]))
```

Some core elements of Numpy are implemented in the C language making 
it super disco fast.


## 2048 Rules

The board is a 4 by 4 matrice (*i.e.* a list of 4 lists of length 4). 
When initialized, all positions are empty except 2 randomly chosen 
positions set to 2.

Then, the player interact with the game by entering a direction (up, down, right, left) and 3 things happens:

- All elements fall such as gravity whose pulling in that direction.
- If two positions with the same value are one under the other when "falling", they merge by adding their values into one single position.
- A new elements pops in a random empty position, of value `2` 80% of the time and of value `4` 20% of the time.

The player looses if no empty position are available to add new elements.

The player wins if one position reach the value 2048.

You must implement the game's logic and not merely the examples given as 
illustrations of the exercises which don't cover all possible cases.


## Exercise 1 :: Initiate the grid

Provide the function `init_grid()` that returns a random board 
for starting the game.

The correction robot will import your script and execute 
the `init_grid()` function, expecting something like:

```python
>>> import numpy as np
>>> from solution import *
>>> grid = init_grid()
>>> print(grid)
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 2]
 [0 0 0 2]]
>>> type(grid)
<class 'numpy.ndarray'>
```

## Exercise 2 :: Add new element to the grid

Provide the function `add_new(grid)` that will add either a 2 (80% of the time) 
or a 4 (20% of the time) somewhere empty in any board. 
If no empty position is available, `add_new` should 
just return the board passed as argument.

```python
>>> import numpy as np
>>> from solution import *
>>> grid = init_grid()
>>> print(grid)
[[0 0 0 0]
 [2 0 2 0]
 [0 0 0 0]
 [0 0 0 0]]
>>> grid = add_new(grid)
>>> print(grid)
[[0 0 0 0]
 [2 0 2 0]
 [0 0 0 4]
 [0 0 0 0]]
>>> type(grid)
<class 'numpy.ndarray'>
```

## Exercise 3 :: Roll some row

Provide the function `rollin_row(row)` that will roll 
the row to the left and returns it, such as:

```python
>>> from solution import *
>>> row = [2, 0, 0, 2]
>>> row = rollin_row(row)
>>> print(row)
[4, 0, 0, 0]
>>> row = [2, 4, 4, 2]
>>> row = rollin_row(row)
>>> print(row)
[2, 8, 2, 0]
```

Here it doesn't matter if `row` is a numpy object or a classic python list.

## Exercise 4 :: Roll the grid

Provide the function `rollin(grid, direction)` where `grid` is the grid to be 
moved and `direction` the direction to be taken, 
`l` (left), `r` (right), `u` (up) and `d` (down). 

`rollin` should return the new grid.

```python
>>> print(grid)
[[ 8  0 16  0]
 [ 4  0  0  0]
 [ 4  0  2  0]
 [ 0 32  2  0]]
>>> grid = rollin(grid, 'd')
>>> print(grid)
[[ 0  0  0  0]
 [ 0  0  0  0]
 [ 8  0 16  0]
 [ 8 32  4  0]]
>>> type(grid)
<class 'numpy.ndarray'>
```

## Exercise 5 :: Create an interactive 2048 game !

!!! note
    This part is not mandatory

You have already built important elements of the game. A few things still need to be done, among which:

+ add a new element (2 or 4) at each turn, when possible
+ Make it playable from a terminal according to player's [inputs](https://docs.python.org/fr/3/library/functions.html#input)
+ Handle when the grid is stuck or a wrong command is entered, why not with [Exceptions](https://docs.python.org/3.4/tutorial/errors.html)
+ Analyse the grid to know when the user wins or looses.

Provide the function `my2048()` that let the user play 2048, such as:

```python
>>> my2048()
[[0 0 0 2]
 [0 0 0 0]
 [0 0 0 0]
 [0 0 0 2]]
u
[[0 0 2 4]
 [0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
l
[[2 4 0 0]
 [0 0 0 0]
 [2 0 0 0]
 [0 0 0 0]]
l
The grid is stuck.
Move in another direction.
[[2 4 0 0]
 [0 0 0 0]
 [2 0 0 0]
 [0 0 0 0]]
u
[[4 4 0 0]
 [0 2 0 0]
 [0 0 0 0]
 [0 0 0 0]]
e
Unknown command.
Press l, r, u or d + Enter.
[[4 4 0 0]
 [0 2 0 0]
 [0 0 0 0]
 [0 0 0 0]]
r
[[0 0 0 8]
 [0 0 2 2]
 [0 0 0 0]
 [0 0 0 0]]
```

```python
[[ 2  8  8  4]
 [ 8 32 16 64]
 [16  8  4  2]
 [ 8  4  2  4]]
l
[[ 2 16  4  4]
 [ 8 32 16 64]
 [16  8  4  2]
 [ 8  4  2  4]]
l
[[ 2 16  8  2]
 [ 8 32 16 64]
 [16  8  4  2]
 [ 8  4  2  4]]
Game Over ! :(
```

## Exercise 6 :: Make python play for you !

!!! note
    This part is not mandatory

Provide another version of `my2048()` named `ai2048()` that will choose itself which direction to go until the game ends.

**Super disco Bonus** :: make an AI that wins !
