
@register_to_all
    Test goal
        Test of python wraps function in functools module to manipulate the module to which the function to be wrapped is belonged.

    Usage
        Add a function to "____all____" of module when defining the function. Since a developer doesn't need to edit the code in two place for one function, using this @register_to_all wrapper can reduce mistake.
        Though IDE won't like it.

    Result
        Success
        But not sure whether it's a good practice to use the frame and stack information of python which are usually controlled by python vm not developer.


@register_builder
    Added in Jan 3rd.
    Since inspecting stack frame of python in runtime for functionality is not a good practice, a builder for wrapper is defined in common. This takes a __all__ list as an argument and returns a wrapper.

