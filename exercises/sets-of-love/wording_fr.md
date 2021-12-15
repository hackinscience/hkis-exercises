## From Pyris, with love.

Once upon a time, in Paris, the city of romance, Bob and Alice met and fall in love with each other.

![Love](https://cdn4.iconfinder.com/data/icons/small-n-flat/24/heart-128.png)


## Exercise 1

To fullfill their romance, they want to meet as much as possible. They share their daily paths among Paris districts to know where they can find each other at the same place.

As you know there is 20 districts in Paris: `['I', 'II','III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX']`.

Code a function named `love_meet` taking bob and alice's daily paths as 2 lists and returning a set of the districts they both visit during the day.

```ipython
In [1]: from solution import love_meet

In [2]: alice = ['II', 'IV', 'II', 'XIX', 'XV', 'IV', 'II']

In [3]: bob = ['IV', 'III', 'II', 'XX', 'II', 'XX']

In [4]: love_meet(bob, alice)
Out[4]: {'II', 'IV'}
```

## Exercise 2

Time goes on, and love goes by...

![broke](https://image.flaticon.com/icons/png/128/805/805031.png)

Alice is bored and get a crush for the strong and handsome Silvester. In order to have an affair with Silvester she must find out where both Silvester and her go during the day. But to avoid an unfortunate encounter with Bob, she must be sure Bob doesn't go there also.

For the sake of her new love, provide Alice the function `affair_meet` that takes Bob, Alice and Silvester daily path in Paris, and returns a set of all places where Alice and Silvester can meet and be sure Bob won't be.

```ipython
In [1]: from solution import affair_meet

In [2]: alice = ['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ']

In [3]: bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']

In [4]: silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']

In [5]: affair_meet(bob, alice, silvester)
Out[5]: {'ⅩⅠⅩ'}
```
