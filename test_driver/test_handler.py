import inject
from cloudshell.configuration.cloudshell_cli_bindings import CLI_SERVICE


class TestHandler:
    @inject.params(cli=CLI_SERVICE)
    def send_dd(self, cli=None):
        out = cli.send_command('ls')
        return out
