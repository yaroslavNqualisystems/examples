from cloudshell.networking.juniper.junos.resource_driver.junos_resource_driver import JunosResourceDriver
from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails, \
    ConnectivityContext

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

context = ResourceCommandContext()
context.resource = ResourceContextDetails()
context.resource.name = 'dsada'
context.reservation = ReservationContextDetails()
context.reservation.reservation_id = 'test_id'
context.resource.attributes = {}
context.resource.attributes['User'] = 'yar'
context.resource.attributes['Password'] = 'Blt0k0ubz'
context.resource.attributes['host'] = 'localhost'
context.resource.address = 'localhost'
context.connectivity = ConnectivityContext()
context.connectivity.admin_auth_token = 'asdas'
context.resource.attributes['SNMP Version'] = '2'
context.resource.attributes['SNMP Read Community'] = 'stargate'


context1 = ResourceCommandContext()
context1.resource = ResourceContextDetails()
context1.resource.name = 'dsada'
context1.reservation = ReservationContextDetails()
context1.reservation.reservation_id = 'test_id'
context1.resource.attributes = {}
context1.resource.attributes['User'] = 'yar'
context1.resource.attributes['Password'] = 'Blt0k0ubz'
context1.resource.attributes['host'] = 'localhost'
context1.resource.address = 'localhost'
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
context2.resource.attributes['User'] = 'yar1'
context2.resource.attributes['Password'] = 'Blt0k0ubz'
context2.resource.attributes['host'] = 'localhost'
context2.resource.address = 'localhost'
context2.connectivity = ConnectivityContext()
context2.connectivity.admin_auth_token = 'asdas'
context2.resource.attributes['SNMP Version'] = '2'
context2.resource.attributes['SNMP Read Community'] = ''



# from cloudshell.shell.core.context_utils import ContextFromArgsMetaclass
#
#
# class DD(object):
#   __metaclass__ = ContextFromArgsMetaclass
#   def test(self):
#     pass
#
#
# class FF(DD):
#   pass
#
# dd = FF()

# print(JunosResourceDriver.mro())

driver = JunosResourceDriver()


# print(getattr(driver, 'send_custom_command'))
driver.initialize(context1)
driver.send_custom_command(context, 'show version')

# driver.ApplyConnectivityChanges(context2, request)
