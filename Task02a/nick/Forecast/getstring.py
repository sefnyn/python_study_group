

def get(message, name="string", default=None):
    message += ": " if default is None else " [Default: {0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            my_str = str(line)
            return my_str
        except ValueError as err:
            print("ERROR", err)

