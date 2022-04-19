![decohints](https://github.com/gri-gus/decohints/blob/main/assets/images/cover.png?raw=true)

# decohints

[🇺🇸 **English version**](README.eng.md)

Декоратор для декораторов, который позволяет видеть параметры задекорированной функции при ее использовании в PyCharm.

**PyPi**: https://pypi.org/project/decohints/

## Причины создания

Ниже показан пример декоратора с параметрами, без использования `decohints`:

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

Если ввести ниже `test()` в PyCharm и подождать, то он подскажет параметры обертки в декораторе как параметры
функции `test`:

<img src="https://github.com/gri-gus/decohints/blob/main/assets/images/1.png?raw=true" width="150" height="105" alt="test() (*args, **kwargs)">

Это не удобно и может запутать разработчиков, поэтому была сделана эта библиотека.

## Установка

```shell
pip install decohints
```

## Использование

✅ Работает со всеми видами декораторов

⚠️ Если ваш декоратор уже обернут в другой декоратор, то `decohints` должен быть верхним

Чтобы воспользоваться, нужно выполнить два простых шага:

1. Импортировать декоратор `decohints` из библиотеки `decohints`:

```python
from decohints import decohints
```

2. Обернуть свой декоратор декоратором `decohints`:

```python
@decohints
def your_decorator():
    ...
```

Ниже показан пример декоратора с параметрами, с использованием `decohints`:

```python
from functools import wraps

from decohints import decohints


@decohints
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


@decorator_without_params
def test(a: int, b: int) -> int:
    return a + b
```

Если ввести ниже `test()` в PyCharm и подождать, то он подскажет параметры функции `test`:

<img width="150" height="105" src="https://github.com/gri-gus/decohints/blob/main/assets/images/2.png?raw=true" alt="test() (a: int, b: int)">

❕Примеры использования с классами-декораторами, декораторами классов и другие находятся
тут: [click](https://github.com/gri-gus/decohints/tree/main/examples/decohints)

## Альтернативные решения

### Указание типа wrapper

✅ Работает со всеми видами функций-декораторов

Если указать тип `wrapper: func`, то будет такое же поведение, как с использованием `decohints`.

Пример:

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

Если ввести ниже `test()` в PyCharm и подождать, то он подскажет параметры функции `test`:

<img width="150" height="105" src="https://github.com/gri-gus/decohints/blob/main/assets/images/2.png?raw=true" alt="test() (a: int, b: int)">

### Указание выходного типа в декораторе с параметрами

❗️Данный способ работает только в функциях-декораторах с параметрами

Если указать тип `Callable` из модуля `typing` для результата декоратора с параметрами, то будет такое же поведение, как
с использованием `decohints`.

Пример:

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

Если ввести ниже `test()` в PyCharm и подождать, то он подскажет параметры функции `test`:

<img width="150" height="105" src="https://github.com/gri-gus/decohints/blob/main/assets/images/2.png?raw=true" alt="test() (a: int, b: int)">
