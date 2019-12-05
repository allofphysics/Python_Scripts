def get_file_paths(start_pos='.'):
    #https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
    import os
    paths = []
    for path, subdirs, files in os.walk(start_pos):
        for name in files:
            resp = os.path.join(path, name)
            paths.append(resp)
    return paths

def get_file_checksums(file_name):
    try:
        import hashlib
        f = open(file_name,'rb')
        data = f.read()
        f.close()
        m = hashlib.sha512()
        m.update(data)
        return {file_name,m.hexdigest()}
    except Exception as e:
        print(e)
        
file_paths = get_file_paths()    
get_file_checksums(file_paths[0])
