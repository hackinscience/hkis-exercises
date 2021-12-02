First, download or clone the [francejs git repository](https://github.com/francejs/irc-bot). 
Then, concatenate all
logs files in the `logs` folder into a single `francejs.csv` file.
Just for your information, this file should contain more than 36,000 lines.

You'll write a program parsing this file (using the `csv` Python
module), to find out and print which pair of nicknames mention each other
the most, like:

```bash
$ python3 solution.py
mdk, sizeof
```

Beware, I may test with another dataset (of the exact same format).


## Data format of this csv file

There's 4 columns:
 - Message type (1 means it's a message, other values means it's a system info, we ignore them)
 - Timestamp of the message (number of seconds since 1st jan 1970 UTC)
 - Username involved
 - Actual message

For example, this line has no interest, it simply logs the arrival of a user,
notice the `2` in the fist column, meaning it's a system info, not a text message:
```text
2,1382426750452,"_mlb","_mlb join the chan."
```

Here, user `_kud` mentions user `nfroidure` on the third line, that's what we're searching for:
```text
1,1382442768956,"nfroidure","pour effroi, je précise"
1,1382442902196,"fbentz","o/"
1,1382443055876,"_kud","On devrait sponsoriser effroi par morsay, nfroidure"
```
