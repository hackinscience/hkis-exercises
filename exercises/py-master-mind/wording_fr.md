## About the game

During this exercise you will implement the [Master
Mind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) game.

The game is about cracking a code of colors chosen by the program,
given we know its length and the possible colors its made of.
At each attempt, the player is given feedback on how well he performed,
so he can improve its next guess.


## Example

We'll represent colors by uppercase letters,
starting at the begining of the alphabet. Therefore, if asked to generate a
code of **size 4** with **six colors 'ABCDEF'**, such as, for example:

```
$ python solution.py
Possible colors are ABCDEF
Code is size 4.
CODE = BFEB
0 --> ABCD
(0, 1)
1 --> BFDE
(2, 1)
2 --> BFEB
Congrats, you won after 3 attempts !
```

The player is given feedback with a
[`tuple`](https://docs.python.org/fr/3/tutorial/datastructures.html#tuples-and-sequences)
of length 2. The first element indicates the number of elements in
the correct position AND color. The second number indicates the number of elements
with the right color BUT in a wrong position.


# Exercises

### Generate colors

You must provide a function `gen_colors(code_size)` taking the number
of colors as parameter and returning a string of the corresponding
uppercase letters.  If the argument is superior to the number of
letters in the alphabet, it should only return the 26 letters of the
alphabet. Such as:

```ipython
In [2]: gen_colors(6)
Out[2]: 'ABCDEF'

In [4]: gen_colors(295)
Out[4]: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
```


### Generate the code

You must provide a function `gen_code(code_size, colors)` taking the
code size and the string containing all colors as parameters and
returning a random generated code.  Such as:

```ipython
In [5]: gen_code(4, 'ABCDEF')
Out[5]: 'DCBF'
```

### Check guess

You must provide a function `check_guess(guess, code_size, colors)`
taking the guess, the code size and the string of colors as
parameters.  The function should check if the guess has the same
length as the code, and if each of its colors is part of the colors'
list.  Such as:

```ipython
In [6]: check_guess('ZZZZ', 4, 'ABCDEF')
Out[6]: False

In [7]: check_guess('EEBBAA', 4, 'ABCDEF')
Out[7]: False

In [8]: check_guess('AABB', 4, 'ABCDEF')
Out[8]: True
```


### Score guess

You must provide a `score_guess(code, guess)` function taking the
code and the guess as parameters and returning a tuple indicating:

1. The number of elements in the right position AND color
2. The number of elements with the right color BUT in a wrong position.

```ipython
In [9]: score_guess('ABCD', 'ABCD')
Out[9]: (4, 0)

In [10]: score_guess('AAAA', 'ABCD')
Out[10]: (1, 0)

In [11]: score_guess('AADA', 'ABCD')
Out[11]: (1, 1)

In [12]: score_guess('ADDA', 'ABCD')
Out[12]: (1, 1)

In [13]: score_guess('ADDB', 'ABCD')
Out[13]: (1, 2)
```

### Play on the command-line

Put it all together ! You must provide a function `play_cli(code_size,
nb_colors)` taking the size of the code and the number of colors as
parameters, and enabling one to play such as:

```
$ python solution.py
Possible colors are ABCDEF
Code is size 4.
0 --> FFRJ
Wrong size or color !
0 --> FFFFF
Wrong size or color !
0 --> ABCD
(0, 0)
1 --> FFEE
(3, 0)
2 --> FFFE
Congrats, you won after 3 attempts !
```
