# from cloudshell.shell.core import driver_config as config
from collections import OrderedDict
from cloudshell.cli.session.session_creator import SessionCreator
from cloudshell.cli.session.session_proxy import ReturnToPoolProxy
from cloudshell.cli.session.ssh_session import SSHSession
from cloudshell.shell.core.context_utils import get_attribute_by_name_wrapper, get_resource_address
from examples.test_driver.test_handler import TestHandler
from cloudshell.configuration.cloudshell_cli_configuration import CONNECTION_TYPE_SSH



HANDLER_CLASS = TestHandler


"""Connection map, defines SessionCreator objects which used for session creation"""
CONNECTION_MAP = OrderedDict()

"""Definition for SSH session"""
ssh_session = SessionCreator(SSHSession)
ssh_session.proxy = ReturnToPoolProxy
ssh_session.kwargs = {'username': get_attribute_by_name_wrapper('User'),
                      # 'password': get_decrypted_password_by_attribute_name_wrapper('Password'),
                      'password': get_attribute_by_name_wrapper('Password'),
                      'host': get_resource_address}
CONNECTION_MAP[CONNECTION_TYPE_SSH] = ssh_session

# GG="dsd"
# ERROR_LIST = ['dsd', 'dddddd']