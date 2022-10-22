# affine

An affine cipher is a function of the form
$f(m) = am + b \pmod n,$
where $a, b, n \in \mathbb{Z}$ and $a$ and $n$ are coprime.
These ciphers can be decrypted using the fact that $a$ has a multiplicative inverse in the ring $\mathbb{Z}/n\mathbb{Z}$. 
In this implementation, $n = 1114112 = 2^{16} \cdot 17^1$ so that any unicode message can be encrypted/decrypted.

## How to Use
Run the file, and then type ```h``` for a list on commands (which are pretty self-explanatory). You can customise your choice of 
$a$ and $b$ by entering them (space separated) in the ``codes.txt`` file.

## Requirements
pyperclip https://pypi.org/project/pyperclip/
