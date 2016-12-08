import threading
import time

from examples.test_driver.test_driver import TestDriver
from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, \
    ReservationContextDetails, ConnectivityContext

class DriverCommandExecution(threading.Thread):
    def __init__(self, driver_instance, command_name, parameters_name_value_map):
        threading.Thread.__init__(self)

        self._parameters_name_value_map = parameters_name_value_map
        self._driver_instance = driver_instance
        self._command_name = command_name
        # self._cancellation_context = CancellationContext()

    def run(self):
        self._result = self._driver_instance.invoke_func(self._command_name,
                                                         self._parameters_name_value_map)

    def set_cancellation_context(self):
        # self._cancellation_context.is_cancelled = True
        pass

    def get_result(self):
        return self._result


class DriverWrapper:
    def __init__(self, obj):
        self.instance = obj

    def invoke_func(self, command_name, params):
        func = getattr(self.instance, command_name)

        return func(**params)


tt = TestDriver()

# dd = DriverWrapper(TestDriver())

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


# def print_result(list):
#     while len(list) > 0:
#         for obj in list:
#             if not obj.isAlive():
#                 print(obj.get_result())
#                 list.remove(obj)


# def print_pool_size():
#     for i in range(1,20):
#         cm = ConnectionManager()
#         print('Pool size: '+str(cm.get_pool_size()))
#         time.sleep(1)


class MyThread(threading.Thread):

    def __del__(self):
        print('Delete Thread: '+self.getName())


# threading.Thread(target=print_pool_size).start()

# def wait(tt):
#     time.sleep(tt)

# tt.simple_command(context1, '10')
# dd = threading.Thread(target=wait, args=[20])
try:
    MyThread(target=tt.simple_command, args=[context2, '10']).start()
except:
    pass
time.sleep(2)
try:
    MyThread(target=tt.simple_command, args=[context, '10']).start()
except:
    pass

try:
    MyThread(target=tt.simple_command, args=[context2, '10']).start()
except:
    pass

try:
    MyThread(target=tt.simple_command, args=[context2, '10']).start()
except:
    pass

# MyThread(target=tt.simple_command, args=[context, '10']).start()

# threading.Thread(target=tt.simple_command, args=[context, '10']).start()
# threading.Thread(target=tt.simple_command, args=[context, '10']).start()
# threading.Thread(target=tt.simple_command, args=[context, '10']).start()
# dd = threading.Thread(target=tt.simple_command, args=[context, '10'])
# dd.start()

# while dd.is_alive:
#     pass



# print(tt.simple_command(context, '10'))
# tt.simple_command(context, '10')

# logger = get_context_based_logger(context)

# tt = DriverCommandExecution(dd, 'simple_command', {'context': context, 'command': '10'})
# tt.start()

# print(get_result(tt))


# dd = DriverCommandExecution(dd, 'simple_command', {'context': context, 'command': '10'})
# dd.start()
# print_result([tt, dd])
