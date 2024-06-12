from test_wrapper import register_to_all

@register_to_all
def test_without_all():
    print('test_without_all called')