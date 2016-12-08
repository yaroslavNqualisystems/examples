"""Definition for SSH session"""
from collections import OrderedDict

from cloudshell.cli.session.session_creator import SessionCreator
from cloudshell.cli.session.session_proxy import ReturnToPoolProxy
from cloudshell.cli.session.telnet_session import TelnetSession
from cloudshell.configuration.cloudshell_cli_configuration import CONNECTION_TYPE_SSH, CONNECTION_TYPE_TELNET
from cloudshell.networking.cisco.aireos.cli.aireos_ssh_session import AireOSSSHSession
from cloudshell.shell.core.context_utils import get_attribute_by_name_wrapper, get_resource_address, \
    get_attribute_by_name
from cloudshell.configuration.cloudshell_cli_configuration import CONNECTION_MAP

ssh_session = SessionCreator(AireOSSSHSession)
ssh_session.proxy = ReturnToPoolProxy
ssh_session.kwargs = {'username': get_attribute_by_name_wrapper('User'),
                      'password': get_attribute_by_name_wrapper('Password'),
                      'host': get_resource_address}
CONNECTION_MAP[CONNECTION_TYPE_SSH] = ssh_session

CONNECTION_EXPECTED_MAP = OrderedDict({r'[Uu]ser:': lambda session: session.send_line(get_attribute_by_name('User')),
                                       r'[Pp]assword:': lambda session: session.send_line(
                                           get_attribute_by_name('Password'))})

"""Definition for Telnet session"""
telnet_session = SessionCreator(TelnetSession)
telnet_session.proxy = ReturnToPoolProxy
telnet_session.kwargs = {'username': get_attribute_by_name_wrapper('User'),
                         # 'password': get_decrypted_password_by_attribute_name_wrapper('Password'),
                         'password': get_attribute_by_name_wrapper('Password'),
                         'host': get_resource_address}
CONNECTION_MAP[CONNECTION_TYPE_TELNET] = telnet_session

HE_MAX_LOOP_RETRIES = 5