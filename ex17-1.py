import re

line="The ghost that says boo hount the loo"
m=re.findall(".oo",line,re.IGNORECASE)
print(m)
