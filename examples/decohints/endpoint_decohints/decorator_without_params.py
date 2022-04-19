from functools import wraps

from decohints import endpoint_decohints


def decorator_without_params(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception:
            print("Error")
            return
        return result

    return wrapper


@endpoint_decohints
@decorator_without_params
def test(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    test()
