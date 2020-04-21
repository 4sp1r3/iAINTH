import  re
def modifyFileContent(filePath):

    w_str = ""

    #for count, line in enumerate(open(filePath,'r', encoding = 'utf-8')):
    for count, line in enumerate(open(filePath, 'r', encoding='utf-8')):
        if re.search('helk-elasticsearch:9200', line): 
            w_str += 'import sys\n' +  \
                   'sys.path.append(\'.\')\n' + \
                   'from helk_info import HELK_IP\n'
            line = re.sub('helk-elasticsearch', 'HELK_IP + \'', line)



        w_str += line

    with open(filePath, 'w', encoding='utf-8') as f:
        f.write(w_str)

modifyFileContent('test/mordor_empire_test/test_12.A.1.py')