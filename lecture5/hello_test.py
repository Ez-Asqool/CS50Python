from hello import hello


def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("Ez") == "hello, Ez"

#test multiple arguments

def test_multiple_arguments():
    for name in ["Hermaione", "Harry", "Ron"]:
        assert hello(name) == f"hello, {name}"

"""
    #run folder as (test package) rather than a module, make a folder, put tests modules in it 
    and add __init__.py empty file and then you can execute/run test folder by (pytest test)
        
"""