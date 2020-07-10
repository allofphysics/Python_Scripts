import os
import re
from collections import defaultdict
dct = defaultdict(dict)

def listfiles(folder):
    for root, folders, files in os.walk(folder):
        for filename in folders + files:
            if filename.endswith('.py'):
                yield os.path.join(root, filename)

def read_file(path):
    with open(path,'r') as f:
        try:
            data = f.read()
            return data
        except Exception as e:
            print(e)

def strip_multiline_comments(data):
    import re
    if data:
        temp_data=False
        match = re.findall('""".*?"""',str(data),re.DOTALL)
        if match:
            for m in match:
                temp_data = data.replace(m,'')
        match = re.findall("'''.*?'''",str(data),re.DOTALL)
        if match:
            for m in match:
                temp_data = data.replace(m,'')
        if temp_data:
            return temp_data
        return data

def iterate_over_lines(data):
    data_cleaned = strip_multiline_comments(data)
    if data_cleaned:
        for line in data_cleaned.splitlines():
            line_cleaned = re.sub('#.*|>>>.*|=.*|".*?"|\'.*?\'','',line)
            line_cleaned = line_cleaned.strip()
            if line_cleaned:
                tokens = re.split(r'\s+',line_cleaned)
                tokens = [x for x in tokens if x]
                if re.findall('from|import',tokens[0]):
                    if 'import' in tokens:
                        if 'from' in line_cleaned:
                            resp = [x for x in re.split('from',line_cleaned) if x]
                            if resp:
                                resp = resp[0]
                                resp = [x.strip() for x in re.split('import',resp) if x]
                                if ',' not in resp:
                                    if len(resp) == 2:
                                        key = resp[0]
                                        imports[key].append(resp[1])
                                else:
                                        key = resp[0]
                                        imports[key].extend(resp[1].split(','))
                if re.findall('def|class',tokens[0]):
                    if 'def' in tokens[0]:
                        match = re.findall('def(.*?\))',line_cleaned)
                        if match:
                            defs['function_defs'].append(match)
file_list = sorted(list(listfiles('.')),key=lambda x: len(x))
base_dict = defaultdict(dict)

for f_name in file_list:
    imports = defaultdict(list)
    defs = defaultdict(list)
    classes = defaultdict(list)
    data = read_file(f_name)
    iterate_over_lines(data)
    base_dict[f_name].update({'imports':imports})
    base_dict[f_name].update(defs)

for k,v in base_dict.items():
    print(k)
    for key,value in v.items():
        print(key,value)
    print('\n')
