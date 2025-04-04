.. |rb| replace:: :code:`RandomBits`
.. |bitslist| replace:: :code:`[bit1,bit2,...,bitn]`

!!!!!!!!!!!!!!!
RandomBits Docs
!!!!!!!!!!!!!!!

--------
|rb|
--------
|rb| lets you make a string of random bits of a specified length.


__init__ (Constructor)
......................
Arguments:

* :code:`num_of_bits`: the number of random bits

Return Value: (nothing)

get_bits (Getter)
.................
Arguments: (none)

Return Value: |bitslist|

set_bits (Setter)
.................
Arguments:

* |bitslist|

Return Value: (none)

validate
....................
Arguments:

* |bitslist|

Raises InvalidBitsError if bits are invalid.

Return Value: (none)

andGate
.......
Arguments: (none)

Return Value: |bitslist|

orGate
......
Arguments: (none)

Return Value: |bitslist|

notGate
.......
Arguments: (none)

Return Value: |bitslist|

norGate
.......
Arguments: (none)

Return Value: |bitslist|

nandGate
........
Arguments: (none)

Return Value: |bitslist|

xorGate
.......
Arguments: (none)

Return Value: |bitslist|

xnorGate
........
Arguments: (none)

Return Value: |bitslist|

andGate
.......
Arguments: (none)

Return Value: |bitslist|



