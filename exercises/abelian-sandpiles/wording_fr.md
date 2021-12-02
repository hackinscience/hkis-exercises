Simulate gravity applied to a sandpile.

Write a function `apply_gravity` that given a 2D numpy array representing
sand will "apply gravity" on it (and returns nothing):

- Each element of the array is an integer representing the height of the sandpile
- Any "pile" that has 4 or more sand particles on it collapses, resulting in four particles being subtracted from the pile and distributed among its neighbors.


## Example

```python
>>> import numpy as np
>>> sandpile = np.zeros((5, 5), dtype=np.uint32)
>>> sandpile[2, 2] = 16
>>> apply_gravity(sandpile)
>>> print(sandpile)
[[0 0 1 0 0]
 [0 2 1 2 0]
 [1 1 0 1 1]
 [0 2 1 2 0]
 [0 0 1 0 0]]

```


## Resources

[https://en.wikipedia.org/wiki/Abelian_sandpile_model](https://en.wikipedia.org/wiki/Abelian_sandpile_model)


## Bonus on your machine (not tested by Hackinscience)

Use matplotlib to display the result as an image:
```python
apply_gravity(sandpile)
plt.imshow(sandpile)
plt.show()
```

To showcase the results, computed a pile of [2 ** 24 grains of sand](https://mdk.fr/sand.png), beware it took 14 days on my laptop…
