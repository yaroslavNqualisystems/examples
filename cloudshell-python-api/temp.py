class FF(object):
    def __init__(self, tt):
        self.tt = tt

    def __getitem__(self, item):
        return self.tt.get(item)



if __name__ == '__main__':
    dd = FF({1:2,3:4})

    print(dd.get(1))