In this exercise you will learn how to write and read csv files in Python.
You need [Python csv library](https://docs.python.org/3/library/csv.html) to
write this exercise.

### Exercise 1

Create a function `generate_csv(a_list)` that will create a
csv file called `results.csv`.

Your function will be called with a list of tuples (like in the following examples).
The tuples will contains tuples which contains as a first a key and as a second
value the value associated with the key.
The keys will always be the same. You must show this keys in the first line
of your csv. After this line you need to add the values formatted like this :

* a list or a tuple must be string: "a,b,c"
* a date must follow the US Standard: "`month`/`day`/`year`"

You don't need to format the other values.

Your csv must use ',' as separator and '"' as quotechar.

With this example :

```python
In [1]: import datetime

In [2]: from <your_solution> import generate_csv

In [3]: meteo = [(('temperature', 42),
   ...:   ('date', datetime.date(2017, 1, 22)),
   ...:   ('locations', ('Berlin', 'Paris')),
   ...:   ('weather', 'sunny')),
   ...:  (('temperature', -42),
   ...:   ('date', datetime.date(2017, 1, 22)),
   ...:   ('locations', ('Marseille', 'Moscow')),
   ...:   ('weather', 'cloudy'))]

In [4]: generate_csv(meteo)
```

You should have this in your `results.csv`:

```text
temperature,date,locations,weather
42,01/22/2017,"Berlin,Paris",sunny
-42,01/22/2017,"Marseille,Moscow",cloudy
```


### Exercise 2

Create a function `parse_csv()` that will read and parse a csv file.
You need to read a file called `students.csv` which will contain in the first
line the column names and after the values. You need to return a list of
dictionaries which will contain the column name as key and the value as value.

Your function need to parse the csv values like this:

* `Birthdate` column: you need to parse it to `datetime.date` object
* `Marks` column: you need to parse it as a list of integers
* other columns: you need a string

Example with the following `students.csv` file :

```text
Firstname,Lastname,Birthdate,Marks,Comments
Ada,Lovelace,12/10/1815,"4242,1010",The first one
Linus,Torvald,12/28/1969,"42,21",Have a problem with penguin
Theo,De Raadt,05/19/1968,"18,19,20",This guy is just crazy
Dennis,Ritchie,09/09/1941,"20,20,20",Like a boss
Alan,Turing,06/23/1912,"42,42,42",Shouldn't eat apple
```

You should have the following result:

```python
In [1]: from <your_solution> import parse_csv

In [2]: parse_csv()
Out[2]:
[{'Birthdate': datetime.date(1815, 12, 10),
  'Comments': 'The first one',
  'Firstname': 'Ada',
  'Lastname': 'Lovelace',
  'Marks': [4242, 1010]},
 {'Birthdate': datetime.date(1969, 12, 28),
  'Comments': 'Have a problem with penguin',
  'Firstname': 'Linus',
  'Lastname': 'Torvald',
  'Marks': [42, 21]},
 {'Birthdate': datetime.date(1968, 5, 19),
  'Comments': 'This guy is just crazy',
  'Firstname': 'Theo',
  'Lastname': 'De Raadt',
  'Marks': [18, 19, 20]},
 {'Birthdate': datetime.date(1941, 9, 9),
  'Comments': 'Like a boss',
  'Firstname': 'Dennis',
  'Lastname': 'Ritchie',
  'Marks': [20, 20, 20]},
 {'Birthdate': datetime.date(1912, 6, 23),
  'Comments': "Shouldn't eat apple",
  'Firstname': 'Alan',
  'Lastname': 'Turing',
  'Marks': [42, 42, 42]}]
```

That's all folk!
