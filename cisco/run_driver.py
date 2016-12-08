import time
from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails, \
    ConnectivityContext

from cloudshell.networking.cisco.ios.cisco_ios_resource_driver import CiscoIOSResourceDriver

from threading import Thread

address = '192.168.42.235'
user = 'root'
password = 'P0G8gOpDHL0c52ROLdsaVQ=='
enable_password = 'NuCpFxP8cJMCic8ePJokug=='
auth_key = 'h8WRxvHoWkmH8rLQz+Z/pg=='
port = 8029

context = ResourceCommandContext()
context.resource = ResourceContextDetails()
context.resource.name = 'dsada'
context.reservation = ReservationContextDetails()
context.reservation.reservation_id = 'test_id'
context.resource.attributes = {}
context.resource.attributes['User'] = user
context.resource.attributes['Password'] = password
context.resource.attributes['host'] = address
context.resource.attributes['Enable Password'] = enable_password
context.resource.address = address
context.connectivity = ConnectivityContext()
context.connectivity.admin_auth_token = auth_key
context.connectivity.server_address = '10.5.1.2'
context.connectivity.cloudshell_api_port = port
context.resource.attributes['SNMP Version'] = '2'
context.resource.attributes['SNMP Read Community'] = 'stargate'
# context.resource.attributes['CLI Connection Type'] = 'Telnet'
context.resource.attributes['CLI Connection Type'] = 'Telnet'
context.resource.attributes['Sessions Concurrency Limit'] = '3'

context1 = ResourceCommandContext()
context1.resource = ResourceContextDetails()
context1.resource.name = 'dsada'
context1.reservation = ReservationContextDetails()
context1.reservation.reservation_id = 'test_id'
context1.resource.attributes = {}
context1.resource.attributes['User'] = user
context1.resource.attributes['Password'] = password
context1.resource.attributes['host'] = address
context1.resource.address = address
context1.connectivity = ConnectivityContext()
context1.connectivity.admin_auth_token = 'asdas'
context1.resource.attributes['SNMP Version'] = '2'
context1.resource.attributes['SNMP Read Community'] = ''

context2 = ResourceCommandContext()
context2.resource = ResourceContextDetails()
context2.resource.name = 'dsada'
context2.reservation = ReservationContextDetails()
context2.reservation.reservation_id = 'test_id'
context2.resource.attributes = {}
context2.resource.attributes['User'] = user
context2.resource.attributes['Password'] = password
context2.resource.attributes['host'] = address
context2.resource.address = address
context2.connectivity = ConnectivityContext()
context2.connectivity.admin_auth_token = 'asdas'
context2.resource.attributes['SNMP Version'] = '1'
context2.resource.attributes['SNMP Read Community'] = ''



driver = CiscoIOSResourceDriver()


# print(driver.send_custom_command(context, 'sh ver'))
Thread(target=driver.restore, args=(context, 'show ver', 'startup-config', 'Append')).start()
time.sleep(1)
Thread(target=driver.save, args=(context, 'show ver', 'dsds')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()
# Thread(target=driver.send_custom_command, args=(context, 'show ver')).start()