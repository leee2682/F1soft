import os

path = r'F:/NIA73/'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def file_move(path):
    folder_lst = os.listdir(path)

    for file in folder_lst:
        item = path + file
        if os.path.isdir(item):
            file_move(path + file + '/')
        else:
            src = os.path.join(path, file)
            dst = os.path.join(path, file)

            print(file)

file_move(path)
