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


def class_decorator(cls):
    class NewClass:
        def __init__(self, *args, **kwargs):
            self._obj = cls(*args, **kwargs)

        def __getattribute__(self, s):
            try:
                x = super().__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            attr = self._obj.__getattribute__(s)
            if isinstance(attr, type(self.__init__)):
                return decorator_without_params(attr)
            else:
                return attr

    return NewClass


@endpoint_decohints
@class_decorator
class Test:
    def test1(self, a: int, b: int) -> int:
        return a + b

    def test2(self, a: int, b: int) -> int:
        return a + b


if __name__ == '__main__':
    test_class = Test
    test_class.test1()
