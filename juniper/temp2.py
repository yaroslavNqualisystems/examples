import re


def validate(path):
    if r'"' not in path:
        path = '\"{}\"'.format(path)
    return path


path = 'tfpt://10.2.5.1/dsdsd/dsf/gggf gfgfg'
print(validate(path))
