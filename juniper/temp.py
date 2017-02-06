from abc import abstractmethod, ABCMeta, abstractproperty


class StructureEntity(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def add_sub_resource(self):
        pass


class PortAttributes(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass


class Port(PortAttributes, StructureEntity):

    def name(self):
        super(Port, self).name()

    def add_sub_resource(self):
        super(Port, self).add_sub_resource()


if __name__ == '__main__':
    port = PortAttributes()
    port.name = 123
