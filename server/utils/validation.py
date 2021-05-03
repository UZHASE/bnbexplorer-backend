import inspect
from functools import wraps


def no_none_args(func):
    """Decorator to check if arguments are None.

    Usage:

    @no_none_args
    def method(param1, param2): ...
    """

    @wraps(func)
    def decorated(*args, **kwargs):
        # get parameter names and values
        names = inspect.getfullargspec(func).args
        values = inspect.getargvalues(inspect.currentframe()).locals.get("args")

        for name, value in zip(names, values):
            if value is None:
                raise ValueError('Invalid value "{}" for parameter "{}"!'.format(value, name))
        return func(*args, **kwargs)

    return decorated
