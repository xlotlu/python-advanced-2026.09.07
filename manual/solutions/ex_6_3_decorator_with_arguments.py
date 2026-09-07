# Write a decorator retry that accepts a parameter num_times. The decorator will
# modify the behavior of the decorated function:
#
# if an exception occurrs in the decorated function, it will not be
# automatically raised, the function will retry num_times times
# if the function fails in all tries, the last occurring exception should
# still be raised
# A decorator like this one would be useful in a scenario where a certain
# resource isn't available at all times (imagine a server timing out). To
# emulate such a behavior, you can use a function like the one below:
#
# def divide():
#     x = int(input("Enter first number: "))
#     y = int(input("Enter second number: "))
#     return x / y
from functools import wraps


def retry(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, num_times+1):
                try:
                    return func(*args, **kwargs)
                except Exception as ex:
                    if i == num_times:  # last try
                        raise ex
                    else:
                        print(f"Exception occurred: {ex}. Retrying...")
        return wrapper
    return decorator_repeat


@retry(3)
def divide():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return x / y


res = divide()
print(res)
