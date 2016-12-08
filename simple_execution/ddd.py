from dd import SSS
import re

prompt = r'.[#>]\\s*$'

if re.search(prompt, SSS, re.DOTALL):
    print('ok')