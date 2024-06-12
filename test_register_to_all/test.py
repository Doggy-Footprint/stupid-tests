from test_pkg.test_mod_with_all import *
from test_pkg.test_mod_without_all import *
from test_pkg.test_mod_register_builder import *

test_with_all()
test_without_all()
test_register_builder()

"""
Warning in visual studio code because the test functions are dynamically added to test_pkg.test_mod_*.__all__
"""