from hello import hello

'''def test_hello():
    # also can be done simply hello("Jon") == "hello, Jon"
    assert hello("David") == "hello, David"
    assert hello() == "hello, world"  '''

def test_default():
    assert hello() == "hello, world"

def test_argument():
    #assert hello("David") == "hello, David"
    for name in ["Hermoine", "Harry", "Ron"]:
        assert hello(name) == f" hello, {name}"