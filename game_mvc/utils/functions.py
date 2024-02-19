from os import walk
def files_from_path(path):
    return next(walk(path), (None, None, []))[2]

def extract_sub_string(string, prefix='', suffix=''):
    return str.removeprefix(string, prefix).removesuffix(suffix)

def handle_exception(function):
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper