from cloudshell.networking.autoload.networking_autoload_resource_attributes import ChassisAttributes, ModuleAttributes
from cloudshell.networking.autoload.networking_autoload_resource_structure import Chassis, Module, SubModule, \
    RootElement, PortChannel

ch_attr_dict = {ChassisAttributes.SERIAL_NUMBER: lambda: 'dsdsds'}
mod_attr_dict = {ModuleAttributes.VERSION: 'asdad'}

sm_attr_dict = {ModuleAttributes.MODEL: lambda: 'nnnnn'}

root = RootElement({})
# root.build_attributes({})

ch = Chassis(0)
# ch.build_attributes(ch_attr_dict)

mod = Module(1)
mod.build_attributes(mod_attr_dict)

sm = SubModule(2)

sm.build_attributes(sm_attr_dict)

pc = PortChannel(3, 'pc1')
pc.build_attributes({})

ch.modules.append(mod)

mod.sub_modules.append(sm)

root.chassis.append(ch)
root.port_channels.append(pc)

root.build_relative_path(None)

resources = root.get_resources()
attributes = root.get_attributes()

print(resources)
