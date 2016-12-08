import telnetlib

host = '10.5.1.2'
# port = '23'

tn = telnetlib.Telnet(host=host, timeout=10)

tn.write(telnetlib.IAC + telnetlib.WILL + telnetlib.ECHO)

print(tn)