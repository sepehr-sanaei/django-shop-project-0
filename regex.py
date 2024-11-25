import re

pattern_mobile = r"(?:0?9|\+?989)\d{2}\W?\d{3}\W?\d{4}"
number = '9126548745'
mobile_match = re.findall(pattern_mobile, number)
if mobile_match:
    print(number)