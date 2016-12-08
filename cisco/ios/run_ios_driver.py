from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails, \
    ConnectivityContext

from cloudshell.networking.cisco.aireos.aireos_resource_driver import AireOSResourceDriver
from cloudshell.networking.cisco.ios.cisco_ios_resource_driver import CiscoIOSResourceDriver

import run_config

from threading import Thread

request = """{
  "driverRequest" : {
    "actions" : [{
      "connectionId" : "457238ad-4023-49cf-8943-219cb038c0dc",
      "connectionParams" : {
        "vlanId" : "45",
        "mode" : "Access",
        "vlanServiceAttributes" : [{
          "attributeName" : "QnQ",
          "attributeValue" : "False",
          "type" : "vlanServiceAttribute"
        }, {
          "attributeName" : "CTag",
          "attributeValue" : "",
          "type" : "vlanServiceAttribute"
        }, {
          "attributeName" : "Isolation Level",
          "attributeValue" : "Shared",
          "type" : "vlanServiceAttribute"
        }, {
          "attributeName" : "Access Mode",
          "attributeValue" : "Access",
          "type" : "vlanServiceAttribute"
        }, {
          "attributeName" : "VLAN ID",
          "attributeValue" : "45",
          "type" : "vlanServiceAttribute"
        }, {
          "attributeName" : "Virtual Network",
          "attributeValue" : "45",
          "type" : "vlanServiceAttribute"
        }, {
          "attributeName" : "Pool Name",
          "attributeValue" : "",
          "type" : "vlanServiceAttribute"
        }
        ],
        "type" : "setVlanParameter"
      },
      "connectorAttributes" : [],
      "actionId" : "457238ad-4023-49cf-8943-219cb038c0dc_4244579e-bf6f-4d14-84f9-32d9cacaf9d9",
      "actionTarget" : {
        "fullName" : "2950/Chassis 0/FastEthernet0-23",
        "fullAddress" : "192.168.42.235/0/23",
        "type" : "actionTarget"
      },
      "customActionAttributes" : [],
      "type" : "setVlan"
    }
    ]
  }
}"""

# address = '172.29.168.43'
# address = '172.17.2.101:1222'
# address = '172.17.2.101:1223'
# address = '10.5.1.2:1222'
# address = '10.5.1.2:1212'
# address = '10.5.1.2:1223'
address = '192.168.42.235'
user = 'root'
# user = 'admin'
# password = 'P0G8gOpDHL0c52ROLdsaVQ=='
# password = 'C1sco123'
# password = 'C1sco123'
password = 'Password1'
port = 1222
enable_password = 'Password2'
auth_key = 'h8WRxvHoWkmH8rLQz+Z/pg=='
api_port = 8029

context = ResourceCommandContext()
context.resource = ResourceContextDetails()
context.resource.name = 'dsada'
context.resource.fullname = 'TestAireOS'
context.reservation = ReservationContextDetails()
context.reservation.reservation_id = 'test_id'
context.resource.attributes = {}
context.resource.attributes['User'] = user
context.resource.attributes['Password'] = password
context.resource.attributes['host'] = address
context.resource.attributes['Enable Password'] = enable_password
context.resource.attributes['Port'] = port
# context.resource.attributes['Backup Location'] = 'tftp://172.25.10.96/AireOS_test'
context.resource.attributes['Backup Location'] = 'tftp://172.17.3.201'
context.resource.address = address
# context.connectivity = ConnectivityContext()
# context.connectivity.admin_auth_token = auth_key
# context.connectivity.server_address = '10.5.1.2'
# context.connectivity.cloudshell_api_port = api_port
context.resource.attributes['SNMP Version'] = '2'
context.resource.attributes['SNMP Read Community'] = 'public'
# context.resource.attributes['CLI Connection Type'] = 'ssh'
context.resource.attributes['CLI Connection Type'] = 'telnet'
context.resource.attributes['Sessions Concurrency Limit'] = '1'




# driver = AireOSResourceDriver(run_config)
driver = CiscoIOSResourceDriver()

# driver.save(context, '','')
print(driver.send_custom_command(context, 'show run'))
# print(driver.update_firmware(context, 'tftp://yar:pass@10.2.5.6:8435', '/test_path/test_file'))
# dd = driver.get_inventory(context)
# print(dd)
# dd = driver.get_inventory(context)
# print(dd)
# print(driver.get_inventory(context))
# print(driver.save(context, '', 'running'))
# print(driver.save(context, '', 'startup'))
# print(driver.save(context, '', ''))
# print(driver.restore(context, 'tftp://172.25.10.96/AireOS_test/TestAireOS-running-250716-115558', 'running', 'override'))
# print(driver.restore(context, 'tftp://172.17.3.201/TestAireOS-running-260716-112111', 'running', 'override'))
# print(driver.ApplyConnectivityChanges(context, request))
# Thread(target=driver.save, args=(context, '', '')).start()?
# Thread(target=driver.save, args=(context, '', '')).start()
# Thread(target=driver.send_custom_command, args=(context, 'help')).start()
# Thread(target=driver.send_custom_command, args=(context, 'help')).start()
# Thread(target=driver.send_custom_command, args=(context, 'help')).start()
# Thread(target=driver.send_custom_command, args=(context, 'help')).start()
# Thread(target=driver.send_custom_command, args=(context, 'help')).start()
# Thread(target=driver.send_custom_command, args=(context, 'help')).start()
# Thread(target=driver.send_custom_command, args=(context, 'help')).start()
