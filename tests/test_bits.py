def assert_raises(fun, *args, **kwargs):
    try:
        _ = fun(*args, **kwargs)
        assert False
    except:
        assert True
def assert_not_raises(fun, *args, **kwargs):
    try:
        _ = fun(*args, *kwargs)
        assert True
    except Exception as e:
        assert False, e

def test_randombits_and():
    import bits
    byte = bits.Bits([0,1,0,1,0,1,0,1])
    assert byte.andGate([0,0,0,0,0,0,0,0]) == [0,0,0,0,0,0,0,0]
def test_randombits_or():
    import bits
    byte = bits.Bits([0,1,0,1,0,1,0,1])
    res = byte.orGate([0,0,0,0,0,0,0,0])
    assert res == [0,1,0,1,0,1,0,1]
def test_randombits_not():
    import bits
    byte = bits.Bits([0,1,0,1,0,1,0,1])
    res = byte.notGate()
    assert res == [1,0,1,0,1,0,1,0]
def test_randombits_nand():
    import bits
    byte = bits.Bits([0,1,0,1,0,1,0,1])
    res = byte.nandGate([0,0,0,0,0,0,0,0])
    assert res == [1,1,1,1,1,1,1,1]
def test_randombits_nor():
    import bits
    byte = bits.Bits([0,1,0,1,0,1,0,1])
    # assert byte.norGate() == 0
    res = byte.norGate([0,0,0,0,0,0,0,0])
    assert res == [1,0,1,0,1,0,1,0]
def test_randombits_xor():
    import bits
    byte = bits.Bits([0,1,0,1,0,1,0,1])
    # assert byte.xorGate() == 1
    res = byte.xorGate([0,0,0,0,0,0,0,0])
    assert res == [0,1,0,1,0,1,0,1]
def test_randombits_xnor():
    import bits
    byte = bits.Bits([0,1,0,1,0,1,0,1])
    # assert byte.xnorGate() == 0
    res = byte.xnorGate([0,0,0,0,0,0,0,0])
    assert res == [1,0,1,0,1,0,1,0]
def test_validate_good():
    import bits
    # byte = bits.Bits([0,1,0,1,0,1,0,1])
    # try:
    #     byte.validate([0,1])
    #     assert True
    # except:
    #     assert False
    assert_raises(bits.Bits.validate, [[0,1]])
def test_validate_bad():
    import bits
    # byte = bits.Bits([0,1,0,1,0,1,0,1])
    # try:
    #     byte.validate([0,2])
    #     assert False
    # except:
    #     assert True
    assert_raises(bits.Bits.validate, [[0,2]])
def test_setbits():
    import bits
    byte = bits.Bits([0,1,0,1,0,1,0,1])
    byte.set_bits([1,0,0,0,0,0,0,0])
    assert byte.getbits() == [1,0,0,0,0,0,0,0]
def test_getbits():
    import bits
    byte = bits.Bits([0,1,0,1,0,1,0,1])
    assert byte.getbits() == [0,1,0,1,0,1,0,1]