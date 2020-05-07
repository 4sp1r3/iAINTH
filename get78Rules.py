import os
import re
from xlrd import open_workbook
from xlutils.copy import copy

rule_list = os.listdir('rule')

procedures_list = os.listdir('procedures')

rule78_list = [rule for rule in procedures_list if rule not in rule_list]

print(rule78_list)

print(len(rule78_list))
rb = open_workbook('resource/rule78列表.xls')
wb = copy(rb)

for id, rule in enumerate(rule78_list):
    wb.get_sheet(0).write(id, 0, rule)
wb.save('resource/rule78列表.xls')

for rule in rule78_list:
    w_str = ""
    for line in open('procedures/' + rule):
        line = re.sub('helk-elasticsearch', '10.25.23.161', line)
        w_str += line
    
    w_str += 'print(' +'\''+ rule +' \'+' +' str(count))'
    
    with open('rule78/' + rule, 'w') as f:
        f.write(w_str)


