

def get(message, name="float", default=None):
    message += ": " if default is None else " [Default: {0}]: ".format(default)
    while True:
        try:
            line = input(message)
            if not line and default is not None:
                return default
            i = float(line)
            return i
        except ValueError as err:
            print("ERROR", err)

