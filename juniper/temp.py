def ff_decor(func):
    def wrap_ff(*args, **kwargs):
        print('before call')
        result = func(*args, **kwargs)
        print("after call")
        return result

    return wrap_ff


class FFProxy(object):
    def __init__(self, instance):
        self. instance = instance

    def __getattr__(self, item):
        if hasattr(self.instance, item):
            attr = getattr(self.instance, item)
            if callable(attr):
                return ff_decor(attr)
            else:
                return attr
        else:
            raise AttributeError()

def f_decor(cls):
    def dec_func(*args, **kwargs):
        # class DecClass(cls):
        # print(cls.__dict__)
        # __metaclass__ = FFMeta
        # instance = cls(*args, **kwargs)
        instance = cls(*args, **kwargs)
        return FFProxy(instance)

    return dec_func


@f_decor
class FF(object):
    # __metaclass__ = FFMeta
    def do(self):
        pass

#
# class DD(FF):
#     __metaclass__ = FFMeta

if __name__ == '__main__':
    ff = FF()
    print(ff.do())