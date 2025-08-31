import time

# start_time = time.time()
# print("im an expert in python")
# print("im an expert in python")
# print("im an expert in python")
# print("im an expert in python")
# print("im an expert in python")
# print("im an expert in python")
# print("im an expert in python")
# print("im an expert in python")
# print("im an expert in python")
# print(time.time() - start_time)


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(
            f"Function {func.__name__} took {time.time() - start_time} seconds to execute."
        )
        return result

    return wrapper


@timer
def say_hello():
    print("Hello, World!")


say_hello()
