class StructureElement(object):
    def __init__(self, relative_id, resource):
        self.id = relative_id
        self.resource = resource
        self.sub_units = []
        self.relative_path = None

    def build_sub_unit(self, relative_id, resource):
        unit = StructureElement(relative_id, resource)
        self.sub_units.append(unit)
        return unit

    def __str__(self):
        return '{0}: {1}'.format(self.relative_path, self.resource)


class StructureUnitUtils(object):
    @staticmethod
    def recursively_build_relative_path(structure_unit, parent_relative_path=None):
        """
        :param structure_unit:
        :type structure_unit: StructureUnit
        :param parent_relative_path:
        :type parent_relative_path: str
        :return:
        """
        structure_unit.relative_path = StructureUnitUtils.build_relative_path(parent_relative_path, structure_unit.id)
        print(structure_unit)
        for sub_unit in structure_unit.sub_units:
            StructureUnitUtils.recursively_build_relative_path(sub_unit, structure_unit.relative_path)

    @staticmethod
    def build_relative_path(parent_path, path):
        if parent_path:
            relative_path = '{0}/{1}'.format(parent_path, path)
        else:
            relative_path = '{0}'.format(path)
        return relative_path


class Resource(object):
    pass


class Chassis(Resource):

    pass


class Port(Resource):
    pass


if __name__ == '__main__':
    root_unit = StructureElement(1, 'chassis')
    port_unit1 = root_unit.build_sub_unit(2, 'port')
    port_unit2 = root_unit.build_sub_unit(3, 'port')

    StructureUnitUtils.recursively_build_relative_path(root_unit)
