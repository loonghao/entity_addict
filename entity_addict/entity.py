# Import built-in modules
from functools import wraps
from typing import Any
from typing import Callable
from typing import TypeVar
from typing import cast

# Import third-party modules
from addict import Dict as Addict  # type: ignore

# For an explanation of how these type-hints work see:
# https://mypy.readthedocs.io/en/stable/generics.html#declaring-decorators
#
# The goal here is that functions which get decorated will retain their types.
__F = TypeVar("__F", bound=Callable[..., Any])


def entity_addict(func: __F) -> __F:
    """Convert function returns to `Dict`.

    Args:
        func: Function name.

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
    def wrapper(*args: Any, **kwargs: Any) -> Any:
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

    return cast(__F, wrapper)
