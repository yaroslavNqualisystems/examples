from logging import Logger
from cloudshell.core.logger.qs_logger import get_qs_logger
from cloudshell.shell.core.context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails
# from driver import BreakingPointChassisDriver, BreakingPointControllerDriver
from driver import BreakingPointControllerDriver
from mock import patch


def get_context():
    address = '10.5.1.127'
    user = 'admin'
    password = 'admin'
    # port = 1222
    # enable_password = 'NuCpFxP8cJMCic8ePJokug=='
    # auth_key = 'h8WRxvHoWkmH8rLQz+Z/pg=='
    # api_port = 8029

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
    # context.resource.attributes['Enable Password'] = enable_password
    # context.resource.attributes['Port'] = port
    # context.resource.attributes['Backup Location'] = 'tftp://172.25.10.96/AireOS_test'
    context.resource.attributes['Backup Location'] = 'ftp://junos:junos@192.168.85.23'
    context.resource.address = address
    # context.connectivity = ConnectivityContext()
    # context.connectivity.admin_auth_token = auth_key
    # context.connectivity.server_address = '10.5.1.2'
    # context.connectivity.cloudshell_api_port = api_port
    context.resource.attributes['SNMP Version'] = '2'
    context.resource.attributes['SNMP Read Community'] = 'public'
    context.resource.attributes['CLI Connection Type'] = 'ssh'
    context.resource.attributes['Enable SNMP'] = 'False'
    context.resource.attributes['Disable SNMP'] = 'False'
    context.resource.attributes['CLI Connection Type'] = 'ssh'
    context.resource.attributes['Sessions Concurrency Limit'] = '1'
    return context


if __name__ == '__main__':
    logger = get_qs_logger()
    # driver = BreakingPointChassisDriver()
    driver = BreakingPointControllerDriver()
    with patch('driver.get_api') as get_api:
        get_api.return_value = type('api', (object,), {
            'DecryptPassword': lambda self, pw: type('Password', (object,), {'Value': pw})()})()
        result = driver.load_config(get_context(), '0VM_RESTART_CS_AS.bpt')
        print(result)
