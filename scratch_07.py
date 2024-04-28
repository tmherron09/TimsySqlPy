


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f'wrapper executed this before {original_function.__name__}')
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def print_all(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f'{key}: {value}')



# print_all('Hello', 'World', name='John', age=30)

def single_param_type_check(type_to_check: type):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            if len(args) != 1:
                raise ValueError('Only One Argument Allowed')
            if not isinstance(args[0], type_to_check):
                raise ValueError('Argument Must Be An Integer')
            return original_function(*args, **kwargs)
        return wrapper_function
    return decorator_function

@single_param_type_check(type_to_check=int)
def print_only_integers(number: int):
    print(number)

# print_only_integers(500)
# print_only_integers('500')


def wrapper_named_arg_check(field_name:str):
    def decorator_inner(original_function):
        def wrapper_function(**kwargs):
            result = kwargs.get(field_name, 'Not Found!')
            print(result, result.__name__)
            return original_function(**kwargs)
        return wrapper_function
    return decorator_inner

@wrapper_named_arg_check('first_value')
def print_if_found(first_value: int):
    print(f'First Value: {first_value}')
    pass


print_if_found(first_value=1000)