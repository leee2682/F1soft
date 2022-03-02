from glob import escape
import paramiko
import getpass
import random
import os

path = r'F:/119 Sample/03/1/'
move_path = "/home/leee2682/test/"

cli = paramiko.SSHClient()
cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
cli.connect("192.168.80.25", username="leee2682", password="leee2682")

def file_lst(path):
    i = 0
    filename = []
    folder_lst = os.listdir(path)

    for file in folder_lst:
        item = path + file
        if file[2:4] == "00" or file[2:4] == "17" or file[2:4] == "18" or file[2:4] == "19" or file[2:4] == "20" or file[2:4] == "22" or file[2:4] == "33" or file[2:4] == "34" or file[2:4] == "35":
            continue
        else:
            if os.path.isdir(item):
                file_lst(path + file + '/')
            elif os.path.isfile(item):
                filename.append(file)
                i += 1

    if i != 0:
        a = random.sample(range(i), 1110)

        for num in range(len(a)):
            src = os.path.join('/' + path, filename[a[num]])

            stdin, stdout, stderr = cli.exec_command("scp -r {} leee2682@192.168.80.25:{}".format(src, move_path))
            # os.system("sshpass -p leee2682 scp -o StrictHostKeyChecking=no -r {} leee2682@192.168.80.25:{}".format(src, move_path))

            print(stdout.read())

file_lst(path)