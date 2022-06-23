# Password Breaker

Created using Python, this script will guess passwords either in plaintext or hashed if you know the algorithm.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following dependencies

- numpy

Then, run

```bash
python path_to_script
```

## How to Use

The script will prompt you for a hash method (such as plain, SHA256, SHA512, etc.) and a string that was hashed with that method. Then, it will brute force all possible passwords for that hash and return the first one that matches.