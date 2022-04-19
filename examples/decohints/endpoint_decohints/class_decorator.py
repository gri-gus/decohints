from functools import wraps

from decohints import endpoint_decohints


class Decorator:
    def __init__(self, aa=None, bb=None, cc=None):
        self.aa = aa
        self.bb = bb
        self.cc = cc

    def __call__(self, func):
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
@Decorator()
def test(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    test()
