from typing import Callable


def decohints(decorator: Callable) -> Callable:
    return decorator


def endpoint_decohints(decorator):
    return decorator
