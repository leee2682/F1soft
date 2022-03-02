## JSON파일 폴더 구조로 정렬

import os
import os.path
from tqdm import tqdm
import csv
import shutil
import jsonss

## 경로 지정
path = r'C:\Repositories\Python\73\cnt119\20211124\raw'
move_path = r'C:\Repositories\Python\73\cnt119\classifier\119json\s3'

#폴더 생성 함수
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# 119 클래스 -> 리스트 화
List=[]
class_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,21,23,24,25,26,27,28,29,30,31,32,36,37,38]
for i in class_list:
    number="0"+str(i)
    List.append(number[-2:])

# 119 클래스 내 양/불 클래스 폴더 생성
for i in List:
    createFolder(os.path.join(move_path, str(i)))
    createFolder(os.path.join(move_path, str(i), '0'))
    createFolder(os.path.join(move_path, str(i), '1'))

# 폴더내 파일 조회
entries=os.listdir(path)

set2=set(entries)

en_total=len(entries)

failList=[]

with tqdm(total=en_total) as pbar:
    for idx,file in enumerate(entries):
        try:
            data = {}
            with open(os.path.join(path, file), "r", encoding='utf-8') as outfile:
                data = json.load(outfile)
            filename=str(file.split('.')[:-1]) # 파일명 확장자 제외
            classGBN=filename.split('_')[1] #클래스 번호
            vioGBN = str(data["description"]['state'])
            # 파일을 지정한 경로로 이동
            shutil.move(os.path.join(path, file) , os.path.join(move_path, str(classGBN), str(vioGBN), str(file)))
        except:
    #            print('실패',i)
            failList.append(str(i))
            pass
    #        time.sleep(0)
        pbar.update(1)
print('\nFailed List')

if len(failList) !=0 :
    print(len(failList))
else :
    print('None')

# 파일이동에 실패한 파일에 대한 로그
with open(os.path.join(move_path, 'failList.csv'), 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(failList)
