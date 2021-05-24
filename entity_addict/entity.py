# Import built-in module
from functools import wraps

# Import third-party modules
from addict import Dict as Addict  # type: ignore


def entity_addict(func):
    """Convert function returns to `Dict`.

    Args:
        func (object): Function name.

    Example:
        >>> @entity_addict
        >>> def hello_entity_addict():
        >>>     return {'test_key': 'test_value'}
        >>> entity = hello_entity_addict()
        >>> print(entity.test_key)
        test_value

    Returns:
        Dict: Instance "Dict" object.

    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """Wrap function for 'Dict'.

        Args:
            args: Arguments to pass into the wrapper.
            kwargs: Arguments to pass into the wrapper.

        Returns:
            addict.Dict: Instance `Dict` object.

        """
        lists = []
        return_value = func(*args, **kwargs)
        if isinstance(return_value, list):
            for value in return_value:
                if isinstance(value, dict):
                    lists.append(Addict(value))
                else:
                    lists.append(value)
            return lists
        elif isinstance(return_value, dict):
            return Addict(return_value)
        else:
            return return_value

    return wrapper
