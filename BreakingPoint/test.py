class FF(object):
    def __init__(self, idd, name, *args, **kwargs):
        self.idd = idd
        self.name = name

    @property
    def text(self):
        return 'fdfdfdf'

    def __str__(self):
        return str(self.idd) + str(self.name)

    def __add__(self, other):
        return str(self) + other

    def __unicode__(self):
        return str(self.idd) + str(self.name)


if __name__ == '__main__':
    dd = FF('dsdsd', 'fdf')

    print('fdfdf gregre  ' + dd)
