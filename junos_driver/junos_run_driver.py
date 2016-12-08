from cloudshell.shell.core.driver_context import AutoLoadCommandContext, ResourceContextDetails, ConnectivityContext
from cloudshell.networking.juniper.junos.resource_driver.junos_resource_driver import JunosResourceDriver
from examples.juniper.autoload.autoload_debug_data import G_DATA

resource = ResourceContextDetails("Junos", "", 'Resource', '192.168.28.150', '', '', '', {}, '', '')
connectivity = ConnectivityContext('10.5.1.2', '', '', 'fdsfdsfdsfsd')
resource.attributes['SNMP Version'] = '2'
resource.attributes['SNMP User'] = ''
resource.attributes['SNMP Password'] = ''
resource.attributes['SNMP Read Community'] = 'public'
resource.attributes['SNMP Private Key'] = ''

context = AutoLoadCommandContext(connectivity, resource)


driver = JunosResourceDriver()
print(driver.get_inventory(context))

# print(G_DATA['jnxContentsTable'])