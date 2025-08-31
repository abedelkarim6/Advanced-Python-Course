# ---Try *args----
def add_numbers(*args):
    print(args)  # args is a tuple
    return sum(args)


print(add_numbers(1, 2))


# ---Try **kwargs----
def print_user_info(**kwargs):
    print(kwargs)


print_user_info(name="Ali", age=25, country="Lebanon")


# ---Try both together----
def my_func(*args, **kwargs):
    print("Keyword:", kwargs)
    print("Positional:", args)


my_func(1, 2, 3, name="Ali", age=25)
