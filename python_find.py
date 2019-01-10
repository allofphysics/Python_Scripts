#https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files
paths = []
for path, subdirs, files in os.walk('.'):
    for name in files:
        resp = os.path.join(path, name)
        paths.append(resp)
