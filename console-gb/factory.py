from os import name, system

def clear_console():
    """Clear command console"""
    system('cls' if name == 'nt' else 'clear')

def get_controlled_user_input(input_prompt: str, options_and_return_values_dict, error_msg: str, is_repeat_intended: bool):
    """Returns the matching value for the key in options_and_return_values_dict if what user wrote was a valid key
    after input_prompt is shown; otherwise it will print error_msg and the same input will be required if is_repeat_intended 
    equal True.
    If is_repeat_intended == False and there is no matching key on options_and_return_values_dict, None will be returned."""
    while True:
        print(options_and_return_values_dict)
        user_input = input(input_prompt)
        if user_input in options_and_return_values_dict:
            return options_and_return_values_dict[user_input]
        else:
            print(error_msg)
        if not is_repeat_intended:
            return

print(get_controlled_user_input("TypeSomething: ", {"yes": 123, "no": 301416}, "Please type something valid.", False))