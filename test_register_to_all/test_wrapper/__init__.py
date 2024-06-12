import inspect
import functools

def register_to_all(f):
    print('registering...')
    f_module = inspect.getmodule(inspect.stack()[1][0])
    try:
        all_obj = inspect.getattr_static(f_module, '__all__')
        all_obj.append(f.__name__)
        print('registered to __all__')
    except AttributeError as AE:
        print('failed to register to __all__')
        print(f'__all__ does not exist in the module {f_module.__name__}')
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

def register_builder(target):
    def w(f):
        print(f'registering...')
        target.append(f.__name__)
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            return f(*args, **kwargs)
        return wrapper
    return w