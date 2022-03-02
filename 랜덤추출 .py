import random
import shutil
import os

path = r'F:/원천데이터/'
move_path = r'F:/119_Sample/'

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def file_lst(path):
    i = 0
    filename = []

    for folder in os.listdir(path):
        if os.path.isfile(os.path.join(path, folder)):
            filename.append(folder)
            i += 1
        else:
            for file in os.listdir(os.path.join(path, folder)):
                filename.append(file)
                i += 1
    try:
        a = random.sample(range(i), 1278)

        for num in range(len(a)):
            move = move_path + filename[a[num]][2:4] + '/' + filename[a[num]][5:6] + '/'

            src = os.path.join(path, filename[a[num]])
            dst = os.path.join(move, filename[a[num]])

            createFolder(move)

            shutil.copy(src, dst)
    except:
        for file in filename:
            move = move_path + file[2:4] + '/' + file[5:6] + '/'

            src = os.path.join(path, file)
            dst = os.path.join(move, file)

            createFolder(move)

            shutil.copy(src, dst)
file_lst(path)