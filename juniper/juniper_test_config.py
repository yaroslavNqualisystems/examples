from weakref import WeakKeyDictionary
from threading import current_thread
# from cloudshell.cli.session.session_creator import SessionCreator
# from cloudshell.cli.session.session_validation_proxy import SessionValidationProxy
# from cloudshell.cli.session.session_proxy import ReturnToPoolProxy
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.cli.session.telnet_session import TelnetSession
# from cloudshell.configuration.cloudshell_cli_configuration import CONNECTION_MAP, CONNECTION_TYPE_SSH, \
#     CONNECTION_TYPE_TELNET

from cloudshell.shell.core.context_utils import get_resource_address, get_attribute_by_name_wrapper
from cloudshell.snmp.quali_snmp import QualiSnmp
from cloudshell.snmp.quali_snmp_cached import QualiSnmpCached

QUALISNMP_INIT_PARAMS = {'ip': get_resource_address,
                         'snmp_version': get_attribute_by_name_wrapper('SNMP Version'),
                         'snmp_user': get_attribute_by_name_wrapper('SNMP V3 User'),
                         'snmp_password': get_attribute_by_name_wrapper('SNMP V3 Password'),
                         'snmp_community': get_attribute_by_name_wrapper('SNMP Read Community'),
                         'snmp_private_key': get_attribute_by_name_wrapper('SNMP V3 Private Key')}


# file_path = '/tmp/_juniper_snmp_cache'
# file_path = '/tmp/_junos_SRX_220'
# file_path = ''


class SaveCachedChanges(QualiSnmpCached):
    def __init__(self, *args, **kwargs):
        super(SaveCachedChanges, self).__init__(*args, **kwargs)
        # try:
        #     self.override_cache_from_file(file_path)
        # except:
        #     pass

        # def __del__(self):
        #     self.save_cache_to_file_if_changed(file_path)

    # def create_snmp_handler():
    #     kwargs = {}
    #     for key, value in QUALISNMP_INIT_PARAMS.iteritems():
    #         if callable(value):
    #             kwargs[key] = value()
    #         else:
    #             kwargs[key] = value
    # snmp_instance = SaveCachedChanges(**kwargs)
    # snmp_instance = QualiSnmp(**kwargs)
    # return snmp_instance


# SNMP_HANDLER_FACTORY = create_snmp_handler

# ssh_session = SessionCreator(SSHSession)
# ssh_session.proxy = ReturnToPoolProxy
# ssh_session.kwargs = {'username': get_attribute_by_name_wrapper('User'),
#                       'password': get_attribute_by_name_wrapper('Password'),
#                       'host': get_resource_address}
# CONNECTION_MAP[CONNECTION_TYPE_SSH] = ssh_session
#
# """Definition for Telnet session"""
# telnet_session = SessionCreator(TelnetSession)
# telnet_session.proxy = ReturnToPoolProxy
# telnet_session.kwargs = {'username': get_attribute_by_name_wrapper('User'),
#                          # 'password': get_decrypted_password_by_attribute_name_wrapper('Password'),
#                          'password': get_attribute_by_name_wrapper('Password'),
#                          'host': get_resource_address}
# CONNECTION_MAP[CONNECTION_TYPE_TELNET] = telnet_session
# POOL_TIMEOUT = 5
