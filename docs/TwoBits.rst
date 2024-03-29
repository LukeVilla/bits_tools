.. |tb| replace:: :code:`TwoBits`

!!!!!!!!!!!!
TwoBits Docs
!!!!!!!!!!!!

-------
|tb|
-------
|tb| stores two bits and lets you use logic gates on them.

__init__ (Constructor)
......................
Arguments:

* :code:`bit1`: integer, either 0 or 1
* :code:`bit2`: integer, either 0 or 1

Return Value: (nothing)

get_bits (Getter)
.................
Arguments: (none)

Return Value: :code:`[bit1,bit2]`

set_bits (Setter)
.................
Arguments:

* :code:`[bit1,bit2]`

Return Value: (none)

validate (Validator)
....................
Arguments:

* :code:`[bit1,bit2]`

Raises InvalidBitsError if bits are invalid

Return Value: (none)

andGate
.......
Arguments: (none)

Return Value: 1 or 0

orGate
......
Arguments: (none)

Return Value: 1 or 0

notGate
.......
Arguments: (none)

Return Value: :code:`[bit1, bit2]`

norGate
.......
Arguments: (none)

Return Value: 1 or 0

nandGate
........
Arguments: (none)

Return Value: 1 or 0

xorGate
.......
Arguments: (none)

Return Value: 1 or 0

xnorGate
........
Arguments: (none)

Return Value: 1 or 0

andGate
.......
Arguments: (none)

Return Value: 1 or 0