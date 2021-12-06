% cifra(1) | cifra usage documentation

# NAME
**cifra** — Library and console command to crypt and decrypt texts using classic methods.

# SYNOPSIS
|    `$ cifra MODE [-h | --help ]`

# DESCRIPTION
**cifra** is a console command and a python library to cipher and decipher texts
using classic methods. It also performs cryptoattacks against those methods.

# MODES

## Dictionary
Manage dictionaries to perform crypto attacks.

## Cipher
Cipher a text using a key.

|    `$ cifra cipher ALGORITHM_NAME CIPHERING_KEY FILE_TO_CIPHER`

## Decipher
Decipher a text using a key.

|    `$ cifra decipher ALGORITHM_NAME CIPHERING_KEY FILE_TO_DECIPHER`

## Attack
Attack a ciphered text to get its plain text.

# ALGORITHMS
Currently these algorithms are available:

* caesar
* substitution
* transposition
* affine
* vigenere

# BUGS
Report issues at: <https://github.com/dante-signal31/cifra-rust/issues>

# INSTALLATION
To install Cifra refer to its installation instructions: <https://github.com/dante-signal31/cifra/wiki/Installation>

# AUTHOR
Dante Signal31 <dante.signal31@gmail.com>

# SEE ALSO
Website: <https://github.com/dante-signal31/cifra-rust>

# COPYRIGHT
Copyright (c) 2021 Dante-Signal31 <dante.signal31@gmail.com>. All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
following conditions are met:

    1. Redistributions of source code must retain the above copyright notice, this list of conditions and the
    following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
    following disclaimer in the documentation and/or other materials provided with the distribution.
    3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or
    promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.