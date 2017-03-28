from cloudshell.api.cloudshell_api import CloudShellAPISession


class AtomationApiBasedInstabce(object):
    def __init__(self, atomation_api):
        self._atiomation_api = atomation_api


class Attribute(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class AttributeContainer(dict):
    def __init__(self, atomation_api):
        super(AttributeContainer, self).__init__(atomation_api)
        self._attributes = {}

    def append(self):
        pass


class Resource:
    def __init__(self, resource_id, model, name):
        self.resource_id = resource_id
        self.model = model
        self.name = name

    @property
    def attributes(self):
        return AttributeContainer()


class ApiBasedNetworkingModel:
    def __init__(self, context, atomation_api):
        """
        :param context:
        :param atomation_api:
        :type atomation_api: CloudShellAPISession
        """
        self._context = context
        self._atomation_api = atomation_api

    def get_resource(self, ):
        # self._atomation_api.Get


if __name__ == '__main__':
    atomation_api = object()
    context = object()
    # creating of Networking Model instance based on atomation api
    networking_api = ApiBasedNetworkingModel(context, atomation_api)
    switch = networking_api.get_resource()

    # Getting basic attributes
    resource_address = switch.attributes.get_resource_address()
    username = switch.attributes.get_username()
    password = switch.attributes.get_password()

    # Adding new chassis
    chassis = switch.new_chassis(0)

    # add autoload attributes to the chassis
    chassis.attributes.set_name = 'Chassis'
    chassis.attributes.set_model = 'Chassis model'
    chassis.attributes.set_version = '121212'
    chassis.save()

    # getting saved chassis by id
    chassis = switch.get_chassis(0)

    # adding module to the chassis
    module = chassis.new_module(1)
    # setting attributes
    module.attributes.set_model('Module 1')
    module.attributes.set_name('Module name')
    module.attributes.set_version('32ws2')

    # adding new, not defined attribute
    module.attributes.appent('New attribute', 'some value')
    module.save()

    # Find resource by model,
    module = chassis.find(model='Module 1')
    # Or getting module by id
    module = chassis.get_module(1)
    # Adding port to module
    port = module.new_port(1)
    port.attributes.set_model('Port 1')
    port.attributes.set_name('Gigabit port')
    port.save()

    # Saving resource tree
    switch.save()

    # iterate by sub resources, instances of Resource
    for resource in chassis:
        pass

    # iterate by attributes, instances fof Attribute
    for attribute in module.attributes:
        pass

    # sync resource with cloudshell
    switch.update()
