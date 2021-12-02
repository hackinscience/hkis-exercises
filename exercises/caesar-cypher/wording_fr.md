## Description

[Caesar cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is an antique
cryptographic method making some information hidden to whom doesn't have the
key to decrypt it.

Think of the alphabet as an ordered list of letters:

```python
>>> from string import ascii_lowercase
>>> list(ascii_lowercase)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

Each letter has a position in this list. `a` is 1, `b` is 2, `j` is 10, etc...

[Caesar cypher](https://en.wikipedia.org/wiki/Caesar_cipher) hide
information by using a *key* which is a positive number to add to the
position of the original letter, the result being the position of the
encrypted letter.

`a` with `key == 2` gives `c`

If the key brings you to the end of the alphabet, you continue to
count from the begining, such as:

`a` with `key == 28` gives `c`

To decypher, or decrypt, the message, you apply the same procedure
moving backward on the alphabet.



You must provide the functions `caesar_cypher_encrypt(s, key)` and
`caesar_cypher_decrypt(s, key)` where:

+ `s` is a string (letter, word, sentence, etc).
+ `key` is a positive integer, the key of the [caesar cypher](https://en.wikipedia.org/wiki/Caesar_cipher).

Your implementation should only transform uppercase and lowercase ASCII
letters. Special characters, numbers and letters with accents should
not be transformed.

Your function shall not print but return the encoded/decoded string.

If you've written it in a `caesar.py` file, you can test it with:

```python
>>> from caesar import caesar_cypher_encrypt, caesar_cypher_decrypt
>>> caesar_cypher_encrypt("a", 2)
'c'
>>> caesar_cypher_decrypt("c", 2)
'a'
>>> caesar_cypher_encrypt("Python is super disco !", 31)
'Udymts nx xzujw inxht !'
>>> caesar_cypher_decrypt("Udymts nx xzujw inxht !", 31)
'Python is super disco !'
```
