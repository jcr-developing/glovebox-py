# import sys
# sys.path.append("console-gb")

import importlib
module = importlib.import_module("..console-gb/factory")

module.get_controlled_user_input("TypeSomething: ", {"yes": 123, "no": 301416}, "Please type something valid.", False)