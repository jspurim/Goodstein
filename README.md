# Goodstain

This is a simple script to generate *Goodstain sequences* as described in [this video](https://www.youtube.com/watch?v=oBOZ2WroiVY).

To run, navigate in the console to the folder containing the script and execute:

```
$ python goodstain.py
```
The output will be valid LaTeX code.
```
$$ 13 = 2^{2 + 1} + 2^{2} + 1 $$
$$ 108 = 3^{3 + 1} + 3^{3} $$
$$ 1279 = 4^{4 + 1} + 3.4^{3} + 3.4^{2} + 3.4 + 3.1 $$
$$ 16092 = 5^{5 + 1} + 3.5^{3} + 3.5^{2} + 3.5 + 2.1 $$
$$ 280711 = 6^{6 + 1} + 3.6^{3} + 3.6^{2} + 3.6 + 1 $$
$$ 5765998 = 7^{7 + 1} + 3.7^{3} + 3.7^{2} + 3.7 $$
$$ 134219479 = 8^{8 + 1} + 3.8^{3} + 3.8^{2} + 2.8 + 7.1 $$
$$ 3486786855 = 9^{9 + 1} + 3.9^{3} + 3.9^{2} + 2.9 + 6.1 $$
$$ 100000003325 = 10^{10 + 1} + 3.10^{3} + 3.10^{2} + 2.10 + 5.1 $$
$$ 3138428381103 = 11^{11 + 1} + 3.11^{3} + 3.11^{2} + 2.11 + 4.1 $$
```



For additional parameters run:

```
$ python goodstain.py -h
```
```
usage: goodstain.py [-h] [-s S] [-n N]

Generates a Goodstain sequence.

optional arguments:
  -h, --help  show this help message and exit
  -s S        Starting number. (default: 13)
  -n N        Number of iterations to compute. (default: 10)
```
