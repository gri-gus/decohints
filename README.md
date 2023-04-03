<p align="center">
    <a>
        <img src="https://raw.githubusercontent.com/gri-gus/decohints/main/assets/images/cover.png" alt="decohints">
    </a>
</p>

<p align="center">
    <a href="https://pypi.org/project/decohints" target="_blank">
        <img src="https://img.shields.io/pypi/v/decohints" alt="PyPI">
    </a>
    <a href="https://pypi.org/project/decohints" target="_blank">
        <img src="https://static.pepy.tech/badge/decohints" alt="PyPI">
    </a>
    <a href="https://opensource.org/licenses/Apache-2.0" target="_blank">
        <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="PyPI">
    </a>
</p>

# decohints

<a href="https://github.com/gri-gus/decohints/blob/main/README.ru.md" target="_blank"><b>🇷🇺 Версия на русском</b></a>

A decorator for decorators that allows you to see the parameters of a decorated function when using it in PyCharm.

**PyPi**: https://pypi.org/project/decohints/

## Reasons for creation

Below is an example of a decorator with parameters without the use of `decohints`:

```python
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

        return wrapper

    return _decorator


@decorator_with_params()
def test(a: int, b: int) -> int:
    return a + b
```

If you type below `test()` in PyCharm and wait, it will show decorator wrapper parameter hints as `test` function
parameter hints:

<img width="150" height="105" src="https://raw.githubusercontent.com/gri-gus/decohints/main/assets/images/1.png" alt="test() (*args, **kwargs)">

This is not convenient and can confuse developers, which is why this library was made.

## Installation

```shell
pip install decohints
```

## Usage

> ✅ Works with all kinds of decorators \
> ⚠️ If your decorator is already wrapped in another decorator, then `decohints` should be on top

To use, you need to follow two simple steps:

1. Import the `decohints` decorator from the `decohints` library:

```python
from decohints import decohints
```

2. Wrap your decorator with a `decohints` decorator:

```python
@decohints
def your_decorator():
    ...
```

The following is an example of a decorator with parameters, with using `decohints`:

```python
from functools import wraps

from decohints import decohints


@decohints
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

        return wrapper

    return _decorator


@decorator_with_params()
def test(a: int, b: int) -> int:
    return a + b
```

If you type below `test()` in PyCharm and wait, it will show `test` function parameter hints:

<img width="150" height="105" src="https://raw.githubusercontent.com/gri-gus/decohints/main/assets/images/2.png" alt="test() (a: int, b: int)">

> ❕Examples of use with decorator class, class decorators, and more are found at here:
<a href="https://github.com/gri-gus/decohints/tree/main/examples/decohints" target="_blank"><b>click</b></a>

## Alternatives

### Specifying the type of wrapper

> ✅ Works with all kinds of decorator functions

Specifying the type `wrapper: func` will have the same behavior as using `decohints`.

Example:

```python
from functools import wraps


def decorator(func):
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


@decorator
def test(a: int, b: int) -> int:
    return a + b
```

If you type below `test()` in PyCharm and wait, it will show `test` function parameter hints:

<img width="150" height="105" src="https://raw.githubusercontent.com/gri-gus/decohints/main/assets/images/2.png" alt="test() (a: int, b: int)">

### Specifying an output type in a decorator with parameters

> ❗️This method only works in decorator functions with parameters

If you specify the `Callable` type from the `typing` module for the result of the decorator with parameters, then the
behavior will be the same as using `decohints`.

Example:

```python
from functools import wraps
from typing import Callable


def decorator_with_params(aa=None, bb=None, cc=None) -> Callable:
    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception:
                print("Error")
                return
            return result

        return wrapper

    return _decorator


@decorator_with_params()
def test(a: int, b: int) -> int:
    return a + b
```

If you type below `test()` in PyCharm and wait, it will show `test` function parameter hints:

<img width="150" height="105" src="https://raw.githubusercontent.com/gri-gus/decohints/main/assets/images/2.png" alt="test() (a: int, b: int)">
