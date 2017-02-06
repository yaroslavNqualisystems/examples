from collections import defaultdict
from cloudshell.shell.core.driver_context import AutoLoadResource


class AbstractResource(object):
    def __init__(self, shell_name):
        # self.autoload_details = autoload_details
        self.shell_name = shell_name
        self.resources = defaultdict(list)
        self.attributes = {}

    def add_sub_resource(self, path_id, resource):
        self.resources[path_id] = resource


    def set_result(self, relative_path, autoload_details):
        autoload_details.resources.append(AutoLoadResource())
        autoload_details.attributes.append(build_attributes())




