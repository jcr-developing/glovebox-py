from ..src import factory

def test_get_controlled_user_input_no_repeat():
    print("No repeat test")
    assert factory.get_controlled_user_input(
             "Type 'yes' to continue: ", {"yes": 123}, "Please type something valid.", False, True) in [123, None]

def test_get_controlled_user_input_repeat():
    print("Repeat test")
    assert factory.get_controlled_user_input(
                "Type 'yes' to continue: ", {"yes": 123}, "Please type something valid.", True, True) == 123