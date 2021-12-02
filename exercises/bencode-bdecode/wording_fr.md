Expose two functions `bencode` and `bdecode`.

 + `bencode` take one object as a parameter and returns `bytes`.
 + `bdecode` take `bytes` as a parameter and returns an object.

objects may be of `type`:

 + `str`
 + `int`
 + `list`
 + `dict`

You have to follow the `bencode` encoding and decoding algorithm, see
[Wikipedia bencode page](http://en.wikipedia.org/wiki/Bencode).
You'll have to encode and decode strings, use "UTF-8" everywhere and explicitly.


## Hints

You may code other `helper` functions in your module,
functions to help `bencode` and `bdecode` in their work. You also can
store module variables and use them but only
for you to use.
