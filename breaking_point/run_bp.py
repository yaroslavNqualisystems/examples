from logging import Logger

import time

from cloudshell.api.cloudshell_api import CloudShellAPISession
from cloudshell.core.logger.qs_logger import get_qs_logger
from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails, \
    ConnectivityContext
# from driver import BreakingPointChassisDriver
# from driver import BreakingPointControllerDriver, BreakingPointChassisDriver
from mock import patch

# from driver import BreakingPointChassisDriver
from driver import BreakingPointControllerDriver


def get_context():
    address = '10.5.1.127'
    user = 'admin'
    password = 'admin'
    reservation_id = 'b5c298ed-72c4-4379-b86d-4e43eb679b36'
    # port = 1222
    # enable_password = 'NuCpFxP8cJMCic8ePJokug=='
    # auth_key = 'h8WRxvHoWkmH8rLQz+Z/pg=='
    api_port = 8029

    context = ResourceCommandContext()
    context.resource = ResourceContextDetails()
    context.resource.name = 'dsada'
    context.resource.fullname = 'TestAireOS'
    context.reservation = ReservationContextDetails()
    context.reservation.reservation_id = reservation_id
    context.reservation.domain = 'Global'
    context.resource.attributes = {}
    context.resource.attributes['User'] = user
    context.resource.attributes['Password'] = password
    context.resource.attributes['host'] = address
    # context.resource.attributes['Enable Password'] = enable_password
    # context.resource.attributes['Port'] = port
    # context.resource.attributes['Backup Location'] = 'tftp://172.25.10.96/AireOS_test'
    context.resource.attributes['Backup Location'] = 'ftp://junos:junos@192.168.85.23'
    context.resource.address = address
    context.connectivity = ConnectivityContext()
    # context.connectivity.admin_auth_token = auth_key
    context.connectivity.server_address = '10.5.1.2'
    context.connectivity.cloudshell_api_port = api_port
    context.resource.attributes['SNMP Version'] = '2'
    context.resource.attributes['SNMP Read Community'] = 'public'
    context.resource.attributes['CLI Connection Type'] = 'ssh'
    context.resource.attributes['Enable SNMP'] = 'False'
    context.resource.attributes['Disable SNMP'] = 'False'
    context.resource.attributes['CLI Connection Type'] = 'ssh'
    context.resource.attributes['Sessions Concurrency Limit'] = '1'
    return context


def create_api_instance(context):
    return CloudShellAPISession(host=context.connectivity.server_address,
                                username='admin',
                                password='admin',
                                domain=context.reservation.domain)


if __name__ == '__main__':
    logger = get_qs_logger()
    # driver = BreakingPointChassisDriver()
    driver = BreakingPointControllerDriver()
    # test_file = 'TemporaryTest.bpt'
    # test_file = 'Blog_Post_2010-08-20_HTTP_DDoS_Flood_test.bpt'
    test_file = '0VM_RESTART_CS_AS.bpt'
    # test_file = 'DDOS.bpt'
    context = get_context()
    api = create_api_instance(context)
    api.DecryptPassword = lambda pw: type('Password', (object,), {'Value': pw})
    # with patch('driver.get_api') as get_api:
    with patch('bp_controller.runners.bp_runner_pool.get_api') as get_api:
        # get_api.return_value = type('api', (object,), {
        #     'DecryptPassword': lambda self, pw: type('Password', (object,), {'Value': pw})()})()
        # result = driver.load_config(get_context(), test_file)
        get_api.return_value = api
        result = driver.get_inventory(context)
        print result
        driver.load_config(context, test_file)
        driver.start_traffic(context, 'False')
        time.sleep(5)
        driver.stop_traffic(context)
        # driver.keep_alive(context, object())
        # print(driver.get_statistics(context, 'summary', 'json'))
