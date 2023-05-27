 
def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
        function_to_apply: a function taking an iterable.
        iterable: an iterable object (list, tuple, iterator).
    Return:
        A value, of same type of elements in the iterable parameter.
        None if the iterable can not be used by the function.
    """
    try:
        iter(iterable)
    except TypeError:
        raise ValueError(f'{iterable} is not iterable')
    it = iter(iterable)
    value = next(it)
    for element in it:
        value = function_to_apply(value, element)
    return value
