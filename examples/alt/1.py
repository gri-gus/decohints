from functools import wraps


def decorator_with_params(aa=None, bb=None, cc=None):
    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception:
                print("Error")
                return
            return result

        wrapper: func
        return wrapper

    return _decorator


@decorator_with_params()
def test(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    test()

