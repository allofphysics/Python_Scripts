def create_file_index(start_pos='.'):
    #https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
    import os
    file_paths = []
    for path, subdirs, files in os.walk(start_pos):
        for name in files:
            resp = os.path.join(path, name)
            file_paths.append(resp)
    #TODO add prefix option
    file_paths = [x.replace('.\\',os.getcwd()+'\\') for x in file_paths]
    return file_paths

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

def mkdir(path):
    import os
    try:
        os.mkdir(path)
    except Exception as e:
        print(e)
        
def copy_file_named_checksum(file_name,folder_name,file_type):
    import os
    import shutil
    new_file_name = list(get_file_checksum(file_name).values())[0]+'.{}'.format(file_type)
    cwd = os.getcwd()
    copy_path = cwd + '\\' + folder_name + new_file_name
    try:
        print(file_name,copy_path)
        shutil.copy(file_name, copy_path)
    except Exception as e:
        print(e)

def filter_by_filetype(file_type):
    import re
    file_paths = create_file_index()
    resp = [x for x in file_paths if re.findall('\.{}$'.format(file_type),x)]
    return resp

###############################################################################################

mkdir('ML')
file_type = 'ml'
file_paths = filter_by_filetype(file_type)
for src in file_paths:
    try:
        dst = '{}\\'.format(file_type.upper())
        copy_file_named_checksum(src,dst,file_type)
    except Exception as e:
        print(e)
