import re

dd = 'error: configuration check-out failed'
patt = r'[Ee]rror\s+.+'

print(re.search(patt, dd))