# def add(a, b):
#     try:
#         print("function add is called.")
#         return a + b
#     except Exception as e:
#         print("Error in add function:", e)


# def sub(a, b):
#     try:
#         print("function sub is called.")
#         return a - b
#     except Exception as e:
#         print("Error in sub function:", e)


# def mul(a, b):
#     try:
#         print("function mul is called.")
#         return a * b
#     except Exception as e:
#         print("Error in mul function:", e)


# def div(a, b):
#     try:
#         print("function div is called.")
#         return a / b
#     except Exception as e:
#         print("Error in div function:", e)


def log_activity(func):
    def wrapper(*args, **kwargs):
        print(f"function {func.__name__} is called")
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error in {func.__name__} function:", e)

    return wrapper


# lets define a decorator
@log_activity
def add(a, b):
    return a + b


@log_activity
def div(a, b):
    return a / b


@log_activity
def sub(a, b):
    return a - b


@log_activity
def mul(a, b):
    return a * b


print(add(1, 2), div(1, 0), sub(1, 2), mul(1, 2))
