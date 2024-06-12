from test_wrapper import register_to_all

__all__ = []

@register_to_all
def test_with_all():
    print('test_with_all called')

# this function can't be imported by *
def test_with_all_not_registered():
    print('test_with_all_not_registered')