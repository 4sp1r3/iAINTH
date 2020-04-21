import os
from ModifyFileContentAddClass import modifyFileContentAddClass


ruleDir = './procedures_2/'

ruleList = os.listdir(ruleDir)
for file in ruleList:
    filepath = ruleDir + file
    modifyFileDataAddClass(filepath)

