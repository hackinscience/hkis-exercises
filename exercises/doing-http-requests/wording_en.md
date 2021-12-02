## Description

!!! warning
    You should work on this exercise with your own installation of Python,
    on your computer. Learn how for
    [Mac OSX](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Mac-OSX)
    or [Windows](https://framagit.org/hackinscience/hkis-website/wikis/How-to-work-on-an-exercise-from-Windows).

This is a short introduction to
[`requests`](http://www.python-requests.org/en/latest/), a Python
module that make grabbing content from the web quite easy.

Requests is _NOT_ in the python distribution, but is installed in HackInScience.

To install it on your machine, use: `python3 -m pip install requests`.

Now, your exercice will just have to
[`GET`](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods)
the content of the page `https://api.github.com/users/python`, and
print it.

In case your computer is not connected to the internet, your program
should simply print `No internet connectivity.` on the standard output.

Beware: requests will raise an exception if there's no internet
connectivity, and I will test this case!

## References

- Requests: <https://requests.readthedocs.io>

## Example

```ipython
$ python solution.py
{
  "login": "python",
  "id": 1525981,
  ...
```

Oh Damn ! The Wi-Fi is down !

```ipython
$ python solution.py
No internet connectivity.
```
