def check_value(allowed_values):
    def decorator(func):
        def wrapper(self, new_value):
            if new_value not in allowed_values:
                raise ValueError("Invalid value")

            return func(self, new_value)

        return wrapper

    return decorator