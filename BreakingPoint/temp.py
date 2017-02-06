import json
from logging import Logger
from cloudshell.traffic_generator.ixia.breaking_point.flows.bp_autoload import BPAutoload
from cloudshell.traffic_generator.ixia.breaking_point.rest_api.rest_session_manager import RestSessionManager
import requests

url = "https://10.5.1.127/api/v1/auth/session"
hostname = '10.5.1.127'
username = 'admin'
password = 'admin'
logger = Logger('dsds')
# json_data = {'username': 'admin', 'password': 'admin1'}
# headers = {'Content-Type': 'application/json'}

manager = RestSessionManager(hostname, username, password, logger)

# l_response = requests.post(url, json=json_data, verify=False)
# cookies = l_response.cookies
# cookies=None

flow = BPAutoload(manager, logger)
# result = flow.get_port_status()
result = flow.do_autoload()
print(result)

# with manager.new_session() as session:
#     port_url = "https://10.5.1.127/api/v1/bps/ports"
#     result = session.request_get(port_url)
#     print(result)

# port_response = requests.get(port_url, cookies=cookies, verify=False)
#
# data = port_response.json()
# # data = json.dumps(port_response.json())
# print(data)
