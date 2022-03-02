import os
import glob
refine=glob.glob('G:/1. 원천데이터셋/*/*/*')
label=glob.glob('G:/2. 라벨링데이터셋/*/*/*')


refine_lst =[]
label_lst =[]

a = 0

for i in refine:
    filename = str(i).split('\\')[-1]
    if filename[7] == '5':
        refine_lst.append(filename)

print(len(refine_lst))

for i in label:
    label_lst.append(str(i).split('\\')[-1].split('.')[0])

print(len(refine_lst), len(label_lst))

print(set(refine_lst) - set(label_lst))
print(set(label_lst) - set(refine_lst))

print(set(refine_lst))