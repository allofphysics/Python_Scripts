from os import listdir 
from sys import argv
import os

master_path = raw_input('master_path')
child_path = raw_input('child_path')

master_path = os.getcwd() + '/' + master_path
child_path = os.getcwd() + '/' + child_path

def create_file_index(start_pos='.'):
    #https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
    import os
    file_paths = []
    for path, subdirs, files in os.walk(start_pos):
        for name in files:
            resp = os.path.join(path, name)
            file_paths.append(resp)
    #TODO add prefix option
    file_paths = [x.replace('./',os.getcwd()+'/') for x in file_paths]
    return file_paths

master_files = create_file_index(master_path)
child_files = create_file_index(child_path)


def get_file_checksum(file_name):
    try:
        import hashlib
        f = open(file_name,'rb')
        data = f.read()
        f.close()
        m = hashlib.md5()
        m.update(data)
        return {file_name:m.hexdigest()}
    except Exception as e:
        print(e)

master_dict={}
for f_name in master_files:
    resp = get_file_checksum(f_name)
    master_dict.update(resp)



child_dict={}
for f_name in child_files:
    resp = get_file_checksum(f_name)
    child_dict.update(resp)

mark_for_deletion = list(set(child_dict.values()).intersection(set(master_dict.values())))

for k,v in child_dict.items():
    if v in mark_for_deletion:
        print(k)
        try:
            os.remove(k)
        except Exception as e:
            print(e)

