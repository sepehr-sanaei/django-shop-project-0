import re

pattern_na_code = r"^[0-9]{10}$"
nc_number = '2846775482'
nc_match = re.findall(pattern_na_code, nc_number)
if nc_match:
    print(nc_number)