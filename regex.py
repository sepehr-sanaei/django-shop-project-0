import re

pattern_name = r"^[\u0600-\u06FF\sA-Za-z]+$"
name_1 = 'sepehr'
name_2 = 'سپهر'
name1_match = re.findall(pattern_name, name_1)
name2_match = re.findall(pattern_name, name_2)
if name1_match and name2_match:
    print(name_1, name_2)