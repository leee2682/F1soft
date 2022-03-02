import os

path = r'F:/dd/'
move_path = r'F:/NIA73/'

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
            move = move_path + file[:6] + '/'

            src = os.path.join(path, file)
            dst = os.path.join(move, file)

            createFolder(move)

            os.rename(src, dst)

file_move(path)
