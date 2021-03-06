import datetime
def logger(old_function):
    def new_function(*args, **kwargs):
        start_time = datetime.datetime.now()
        old_return = old_function(*args, **kwargs)
        end_time = datetime.datetime.now()
        with open('file.txt', 'w') as file:
            file.write(str(start_time) + '\n')
            file.write(str(end_time) + '\n')
            file.write(old_function.__name__ + '\n')
            for arg in args:
                file.write(str(arg) + '\n')
        for kwarg in kwargs:
            kwarg_str = str(kwarg) + '=' + str(kwargs[kwarg])
            file.write(kwarg_str + '\n')
        return old_return
    return new_function