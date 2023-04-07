.. |tb| replace:: :code:`TwoBits`

!!!!!!!!!!!!!!!
bits-tools Docs
!!!!!!!!!!!!!!!

--------
Overview
--------
bits-tools is a Python module that lets you work with individual bits.
It has two main classes: |tb| and :code:`RandomBits`.

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




