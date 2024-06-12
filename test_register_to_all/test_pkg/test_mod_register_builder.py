from test_wrapper import register_builder

__all__ = []
local_register_to_all = register_builder(__all__)

@local_register_to_all
def test_register_builder():
    print('test_register_builder called')
