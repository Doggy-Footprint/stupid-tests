from test_wrapper import register_to_all

# this will be called since there is no explicit __all__. 
# If there is no explicit __all__, 
# all symbols in current module's namespace can be imported with *
@register_to_all
def test_without_all():
    print('test_without_all called')

