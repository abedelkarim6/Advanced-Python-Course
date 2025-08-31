# ---------------------------- broken version ----------------------------


def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """This function says hello"""
    print("Hello!")


print(greet.__name__)  # wrapper ❌
print(greet.__doc__)  # None ❌

# ---------------------------- fixed version ----------------------------

from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


@my_decorator
def greet():
    """This function says hello"""
    print("Hello!")


print(greet.__name__)  # greet ✅
print(greet.__doc__)  # "This function says hello" ✅
